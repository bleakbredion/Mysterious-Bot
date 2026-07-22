from secret import api

async def get_id(message):
    return message.from_id


async def get_user_fullname(message):
    user = await message.ctx_api.users.get(message.from_id)
    if not user:
        return "Unknown user"
    return f"{user[0].first_name} {user[0].last_name}"


async def get_first_name(message):
    user = await message.ctx_api.users.get(message.from_id)
    if not user:
        return "Unknown user"
    return user[0].first_name


async def get_last_name(message):
    user = await message.ctx_api.users.get(message.from_id)
    if not user:
        return "Unknown user"   
    return user[0].last_name
