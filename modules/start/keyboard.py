from vkbottle import Keyboard, Text

start_keyboard = (
    Keyboard(inline=True)
    .add(Text("Меню", payload={'cmd': 'menu'}))
    .row()

    # .add(Text("Кто ночной?", payload={'cmd': 'night'}))
    .row()

    # .add(Text("Рассписание летки", payload={'cmd': 'shedule'}))
    .row()

    # .add(Text("Общая информация про летку", payload={'cmd': 'common_info'}))
    .row()
    
    .add(Text("Погода", payload={'cmd': 'weather'}))
    .row()

    .add(Text("Пригласить комсенка в блок", payload={'cmd': 'invite_komsenok'}))
    .row()


)
