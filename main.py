import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///shop_items.db")
Base = declarative_base()


class Item(Base):

    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column("name", String)
    # amount = Column("amount", Integer)
    # price = Column("price", Float)
    # best_before = Column("best before", DateTime)
    # day_entered = Column("day of creation", DateTime)
    # item_type = Column("type of item", String)


class ManageItems:

    def create_item(self) -> None:
        pass

    def name_to_capitals(self) -> str:
        return self.name.upper()


item_one = Item(name="Rope")

name = ManageItems.name_to_capitals(item_one)

print(name)
