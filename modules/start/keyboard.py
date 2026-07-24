from vkbottle import Keyboard, Text

start_keyboard = (
    Keyboard(inline=True)
    .add(Text("Меню", payload={'cmd': 'menu'}))
    .add(Text("Кто ночной?", payload={'cmd': 'night'}))
    .row()
    .add(Text("Расписание летки", payload={'cmd': 'shedule'}))
    .add(Text("Общая информация", payload={'cmd': 'common_info'}))
    .row()
    .add(Text("Погода", payload={'cmd': 'weather'}))
    .add(Text("Пригласить комсенка", payload={"cmd": "invite_komsenok"}))
    .row()
    .add(Text("Ввести имя пользователя", payload={'cmd': 'add_user_name'}))

)
