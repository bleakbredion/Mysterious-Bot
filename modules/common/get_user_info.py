async def get_id(message):
    return message.from_id


async def get_first_name(message):
    user = await api.users.get(message.from_id)
    return user[0].first_name


async def get_last_name(message):
    user = await api.users.get(message.from_id)
    return user[0].last_name
