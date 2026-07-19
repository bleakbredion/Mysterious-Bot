from vkbottle import Keyboard, Text

back_to_main_menu_keyboard = (
    Keyboard(inline=True)
    .add(Text("На главную", payload={'cmd': 'start'}))
    .row()
)

