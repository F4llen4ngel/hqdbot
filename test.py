from lib.database.database import Database
import sqlalchemy

import asyncio


async def main():
    db = Database()
    await db.init_models()
    await db.add_order(1, "test")
    orders = await db.get_orders(1)
    await db.close()
    for order in orders:
        print(order.id, order.user_id, order.order)
    


if __name__ == "__main__":
    asyncio.run(main())