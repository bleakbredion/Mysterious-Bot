from vkbottle import Keyboard, Text

home_keyboard = (
    Keyboard(inline=True)
    .add(Text("На главную", payload={'cmd': 'start'}))
    .row()
)