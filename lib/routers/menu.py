from vkwave.bots import DefaultRouter, SimpleBotEvent, simple_bot_message_handler, Keyboard, ButtonColor


menu_router = DefaultRouter()
menu_keyboard = Keyboard()
menu_keyboard.add_text_button(text="Каталог🔎", color=ButtonColor.PRIMARY)
menu_keyboard.add_text_button(text="Корзина🛒", color=ButtonColor.POSITIVE)
menu_keyboard.add_row()
menu_keyboard.add_text_button(text="Мои заказы📃", color=ButtonColor.SECONDARY)
menu_keyboard.add_text_button(text="Отзывы⭐", color=ButtonColor.SECONDARY)

@simple_bot_message_handler(menu_router,)
async def menu(event: SimpleBotEvent):
    return await event.answer(
        message="Добро пожаловать в Panda Smoke!🐼\n\n Воспользуйся меню, чтобы продолжить",
        keyboard=menu_keyboard.get_keyboard(),
    )