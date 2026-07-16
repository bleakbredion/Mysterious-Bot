from vkbottle import Keyboard, Text
from config import MAX_DATE


menu_date_keyboard = Keyboard(inline=True)
for i in range(1, MAX_DATE+1):
    menu_date_keyboard.add(
        Text(f'{i}.06', payload={'cmd': f'menu_date_{i}'})
        ).row()


menu_keyboard = (
    Keyboard(inline=True)
    .add(Text("На главную", payload={'cmd': 'start'}))
    .row()
    .add(Text("Назад", payload={'cmd': 'menu_date'}))
)
