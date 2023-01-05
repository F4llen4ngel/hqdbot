from lib.database import service, models, base
import sqlalchemy

import asyncio


async def main():
    print(sqlalchemy.__version__)
    await base.init_models()
    session = await base.get_session()
    await service.add_order(session, 1, "test")
    orders = await service.get_orders(session, 1)
    print(orders)


if __name__ == "__main__":
    asyncio.run(main())