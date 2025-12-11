""" 01 Воспроизведение мультимедиа

Создайте два класса:
Класс 1

AudioFileMixin — требует наличие атрибута audio_tracks (список треков).


Метод play_audio() выводит:
Воспроизведение аудио для <НазваниеКласса>:
	<название трека>
	<название трека>

Класс 2

VideoFileMixin — требует наличие атрибута video_files (список видео).


Метод play_video() выводит:
Воспроизведение видео для <НазваниеКласса>:
	<название видео>
	<название видео>

Если нужное поле отсутствует — выбрасывайте AttributeError.
"""


class AudioFileMixin:
    def play_audio(self):
        if not hasattr(self, "audio_tracks"):
            raise AttributeError("Не задан audio_tracks")
        print(f"Воспроизведение аудио для {self.__class__.__name__}:")
        for track in self.audio_tracks:
            print(track)


class VideoFileMixin:
    def play_video(self):
        if not hasattr(self, "video_files"):
            raise AttributeError("Не задан video_files")
        print(f"Воспроизведение видео для {self.__class__.__name__}:")
        for file in self.video_files:
            print(file)


# Проверим в следующем задании!
