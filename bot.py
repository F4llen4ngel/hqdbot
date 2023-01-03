from vkwave.bots import SimpleLongPollBot

from lib.utils.auth import TOKEN, GROUP_ID

from lib.routers import menu

bot = SimpleLongPollBot(tokens=TOKEN, group_id=GROUP_ID)

bot.dispatcher.add_router(menu.menu_router)

bot.run_forever()