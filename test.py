from lib.database import service, models, base

import asyncio

async def main():
    await base.init_models()
    session = await base.get_session()
    await service.add_order(session, 1, "test")
    orders = await service.get_orders(session, 1)
    print(orders)

asyncio.run(main())