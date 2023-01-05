from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from lib.database.models import *


async def get_orders(session: AsyncSession, user_id: int):
    result = await session.execute(
        select(Order).where(Order.user_id == user_id))
    return result.scalars().all()


async def add_order(session: AsyncSession, user_id: int, order: str):
    new_order = Order(user_id=user_id, order=order)
    session.add(new_order)
    await session.commit()