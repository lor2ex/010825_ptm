from pymongo import MongoClient

URI_READ = 'mongodb://...'
URI_EDIT = 'mongodb://...'


def run_migration():
    try:
        client_read = MongoClient(URI_READ)
        client_edit = MongoClient(URI_EDIT)

        db_read = client_read["ich"]
        db_edit = client_edit["ich_edit"]

        source_coll = db_read["Spotify_Youtube"]

        pipeline_spotify = [
            {"$sort": {"Stream": -1}},
            {"$limit": 20}
        ]

        top_spotify = list(source_coll.aggregate(pipeline_spotify))

        pipeline_youtube = [
            {"$sort": {"Views": -1}},
            {"$limit": 20}
        ]

        top_youtube = list(source_coll.aggregate(pipeline_youtube))

        def save_to_edit(data, target_name):
            if data:
                for doc in data:
                    doc.pop('_id', None)

                db_edit[target_name].drop()
                db_edit[target_name].insert_many(data)
                print(f"Готово! Данные импортированы в ich_edit.{target_name}")

        save_to_edit(top_spotify, "010825_al_top20spotify")
        save_to_edit(top_youtube, "010825_al_top20youtube")

    except Exception as e:
        print(f"Ошибка при выполнении: {e}")
    finally:
        client_read.close()
        client_edit.close()


if __name__ == "__main__":
    run_migration()