import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, AsyncConnection, create_async_engine
from lib.database.models import Order
from lib.database.base import Base


class Database:

    def __init__(self):
        self.DATABASE_URL = "postgresql+asyncpg://hqd_db:hqd_password_1337@localhost/hqd_db"
        self.Engine = create_async_engine(self.DATABASE_URL, echo=False)
        self.Session = AsyncSession(self.Engine, expire_on_commit=False)

    async def init_models(self):
        """Drops all tables and creates new ones."""
        async with self.Engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    async def add_order(self, user_id: int, order: str):
        """Add an order to the database.

        Args:
            user_id (int): The id of the user to add the order to.
            order (str): The order to add.
        """
        new_order = Order(user_id=user_id, order=order)
        self.Session.add(new_order)
        await self.Session.commit()

    async def get_orders(self, user_id: int) -> list:
        """Get orders from user_id from the database.

        Args:
            user_id (int): The id of the user to get orders from.

        Returns:
            list: A list of orders.
        """
        result = await self.Session.execute(select(Order).where(Order.user_id == user_id))
        return result.scalars().all()

    async def remove_order(self, order_id: int):
        """Remove an order from the database.

        Args:
            order_id (int): The id of the order to remove.
        """
        await self.Session.execute(select(Order).where(Order.id == order_id).delete())
        await self.Session.commit()

    async def close(self):
        """
        Closes the database connection. This method should be called when the bot is shutting down.
        """
        await self.Session.close()
        await self.Engine.dispose()