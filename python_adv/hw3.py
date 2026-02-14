from decimal import Decimal

from sqlalchemy import (
    create_engine,
    Integer,
    String,
    Boolean,
    ForeignKey,
    Numeric
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    sessionmaker
)


engine = create_engine('sqlite:///:memory:')

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

class Base(DeclarativeBase):
    __abstract__ = True


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    description: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )

    products = relationship(
        'Product',
        back_populates='category'
    )



class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )
    in_stock: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )
    category_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('categories.id')
    )

    category = relationship(
        'Category',
        back_populates='products'
    )


Base.metadata.create_all(bind=engine)

print("ALL TABLES WAS CREATED")
print(Base.metadata.tables)
