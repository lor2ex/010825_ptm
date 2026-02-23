from flask import Blueprint, jsonify, request
from sqlalchemy import select
from pydantic import ValidationError

from core.db import db
from models.questions import Category
from schemas.questions import (
    CategoryRetrieve,
    CategoryCreate,
    CategoryUpdate
)

categories_bp = Blueprint(
    "categories",
    __name__,
    url_prefix="/categories"
)
# Read (list)
@categories_bp.route("")
def get_all_categories():
    # TODO-LIST:
    # 1. Сдкелть запрос на получения всех оъектов из базы
    stmt = select(Category)
    result = db.session.execute(stmt).scalars()

    # 2. Как-то преобразовать сложный объект ORM в простой словарик python
    response = [
        CategoryRetrieve.model_validate(obj).model_dump()
        for obj in result
    ]

    # response = []
    #
    # for obj in result:
    #     response.append(obj.to_dict())


    # 3. вернуть данные как ответ в JSON формате с правильным status code
    return jsonify(response), 200  # 200 OK


# Read (one by ID)
@categories_bp.route("/<int:category_id>")
def get_category_by_id(category_id: int):
    # 1. Получить один объект
    stmt = select(Category).where(Category.id == category_id)
    category = db.session.execute(stmt).scalars().one_or_none()

    # 2. Проверить, что объект есть в БД
    if not category:
        return jsonify({"error": f"Category with ID {category_id} not found"}), 404  # 404 NOT FOUND


    # 3. Преобразовать в простой словарь и вернуть ответ
    return jsonify(CategoryRetrieve.model_validate(category).model_dump()), 200


# Create
@categories_bp.route("", methods=["POST"])
def create_new_category():
    # https://example.com/category?new=true => request.args -> {"new": True}
    # TODO-LIST для создания объекта
    # 1. Попытаться Получить сырые данные
    raw_data = request.get_json(silent=True)

    # 2. Провести проверки, что данные есть, они валидны, все требуемые колонки указаны
    if not raw_data:
        return jsonify(
            {
                "error": "Request body is missing or not valid JSON"
            }
        ), 400  # 400 BAD REQUEST

    try:
        validated_data = CategoryCreate.model_validate(raw_data)
    except ValidationError as e:
        return jsonify(
            {
                "error": e.errors()
            }
        ), 400

    try:
        # 3. Попытаться создать новый объект
        new_category = Category(**validated_data.model_dump())

        # 4. Добавить объект в сессию
        db.session.add(new_category)

        # 5. Применить изменения из сессии в Базу Данных
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify(
            {
                "error": "Failed to create new category",
                "detail": str(e)
            }
        ), 500  # 500 INTERNAL SERVER ERROR

    # 6. Вернуть ответ
    return jsonify(CategoryRetrieve.model_validate(new_category).model_dump()), 201  # 201 CREATED


# Update
@categories_bp.route("/<int:category_id>", methods=["PUT", "PATCH"])
def update_category_by_id(category_id: int, exclude_unset=None):
    # 1. Попытаться Получить сырые данные
    raw_data = request.get_json(silent=True)

    # 2. Провести проверки, что данные есть, они валидны, все требуемые колонки указаны
    if not raw_data:
        return jsonify(
            {
                "error": "Request body is missing or not valid JSON"
            }
        ), 400  # 400 BAD REQUEST

    try:
        validated_data = CategoryUpdate.model_validate(raw_data)
    except ValidationError as e:
        return jsonify(
            {
                "error": e.errors()
            }
        ), 400

    stmt = select(Category).where(Category.id == category_id)
    category = db.session.execute(stmt).scalars().one_or_none()

    if not category:
        return jsonify({"error": f"Category with ID {category_id} not found"}), 404

    try:
        for key, value in validated_data.model_dump(exclude_unset=True).items():
            setattr(category, key, value)

        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "error": f"Failed to update category with ID {category_id}",
            "detail": str(e)
        }), 500  # 500 INTERNAL SERVER ERROR

    return jsonify(CategoryRetrieve.model_validate(category).model_dump()), 200


# Delete
@categories_bp.route("/<int:category_id>", methods=["DELETE"])
def delete_category_by_id(category_id: int):
    stmt = select(Category).where(Category.id == category_id)
    category = db.session.execute(stmt).scalars().one_or_none()

    if not category:
        return jsonify({"error": f"Category with ID {category_id} not found"}), 404

    try:
        db.session.delete(category)
        db.session.commit()
    except Exception as e:
        db.session.rollback()

        return jsonify({
            "error": f"Failed to delete Category with ID {category_id}",
            "detail": str(e)
        }), 500

    return jsonify({"message": f"Category with ID {category_id} deleted successfully"}), 204  # 204 NO CONTENT
