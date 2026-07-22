from vkbottle import Keyboard, Text

start_keyboard = (
    Keyboard(inline=True)
    .add(Text("Меню", payload={'cmd': 'menu'}))
    .add(Text("Кто ночной?", payload={'cmd': 'night'}))
    .add(Text("Рассписание летки", payload={'cmd': 'shedule'}))
    .add(Text("Общая информация про летку", payload={'cmd': 'common_info'}))
    .row()
    .add(Text("Погода", payload={'cmd': 'weather'}))
    .add(Text("Пригласить комсенка в блок", payload={'cmd': 'invite_komsenok'}))
    .add(Text("Ввести имя пользователя", payload={'cmd': 'add_user_name'}))

)
