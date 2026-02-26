from sqlalchemy import select, func
from sqlalchemy.orm import joinedload

from hw3 import *

engine = create_engine('sqlite:///:memory:')

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
Base.metadata.create_all(engine)

"""Задача 1: Наполнение данными"""

electronics = Category(
    name="Электроника",
    description="Гаджеты и устройства."
)
books = Category(
    name="Книги",
    description="Печатные книги и электронные книги."
)
clothing = Category(
    name="Одежда",
    description="Одежда для мужчин и женщин."
)

smartphone = Product(
    name="Смартфон",
    price=Decimal("299.99"),
    in_stock=True,
    category=electronics,
)
notebook = Product(
    name="Ноутбук",
    price=Decimal("499.99"),
    in_stock=True,
    category=electronics,
)
roman = Product(
    name="Научно-фантастический роман",
    price=Decimal("15.99"),
    in_stock=True,
    category=books,
)
jeans = Product(
    name="Джинсы",
    price=Decimal("40.50"),
    in_stock=True,
    category=clothing,
)
t_shirt = Product(
    name="Футболка",
    price=Decimal("20.00"),
    in_stock=True,
    category=clothing,
)

session.add_all([electronics, books, clothing, smartphone, notebook, roman, jeans, t_shirt])
session.commit()

"""Задача 2: Чтение данных. Извлеките все записи из таблицы categories. 
Для каждой категории извлеките и выведите все 
связанные с ней продукты, включая их названия и цены."""

with Session() as session:
    stmt = (
        select(Category)
        .options(joinedload(Category.products))  # joinedload - ленивая подгрузка(если есть вложеннность-обязательна, ибо грозит эфект n+1(перегрузка базы)
    )
    result = session.scalars(stmt).unique().all()

    for cat in result:
        print(f"Категория: {cat.name}")

        for prod in cat.products:
            print(f" -- Продукт: {prod.name}, Цена: {prod.price}")


# var 2
# categories = session.query(Category).all()
# # --- Teil 3: Alternative Abfrage-Methoden, другие варианты строки выше: ---
# # Diese Zeilen zeigen verschiedene Wege, um alle Kategorien zu laden:
#
# # 1. Empfohlener 2.0 Stil (Direkt über session.scalars)
categories = session.scalars(select(Category)).all()
#
# # 2. Klassischer 1.x Stil (session.query - veraltet, aber noch unterstützt)
# categories = session.query(Category).all()
#
# # 3. Ausführlicher 2.0 Stil (Über session.execute)
# categories = session.execute(select(Category)).scalars()

for c in categories:
    print(c.id, c.name, c.description)

# var 2 cicle for
# for cat in categories:
#     print(cat.id, cat.name, cat.description)
#     for product in cat.products:
#         print("Продукты:", product.id, product.name, product.price)


"""Задача 3: Обновление данных
Найдите в таблице products первый продукт с названием "Смартфон". 
Замените цену этого продукта на 349.99."""

stmt = (
    select(Product)
    .where(Product.name == "Смартфон")
)

result = session.execute(stmt).scalars().first()
print(result.name)

if result:
    result.price=Decimal("349.99")
    session.commit()
    print(result.name, result.price)


# var 2
# product = session.get(Products, ident=1)
# if product:
#     product.price = 349.99
#     session.commit()
#
# product = session.get(Products, ident=1)
# if product:
#     print(product.name, product.price)
"""Задача 4: Агрегация и группировка
Используя агрегирующие функции и группировку, подсчитайте общее 
количество продуктов в каждой категории."""

stmt = (
    select(Category.name, func.count(Product.id))
    .join(Product)
    .group_by(Category.name)
)

result = session.execute(stmt).all()
for name, count in result:
    print(name, count)


"""Задача 5: Группировка с фильтрацией
Отфильтруйте и выведите только те категории, в которых более одного продукта."""

stmt = (
    select(Category.name, func.count(Product.id))
    .join(Product)
    .group_by(Category.name)
    .having(func.count(Product.id) > 1)
)

result = session.execute(stmt).all()
# print(result)
for name, count in result:
    # if count > 1:
        print(name, count)