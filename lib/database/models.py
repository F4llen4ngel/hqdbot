from sqlalchemy import Column, String, Integer
from lib.database.base import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    order = Column(String)

    def __str__(self):
        return f"Order(id:{self.id}, user_id:{self.user_id}, order:{self.order})"