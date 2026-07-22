from vkbottle.dispatch.middlewares import BaseMiddleware

from database.users import add_user


class UserMiddleware(BaseMiddleware):
    async def pre(self):
        await add_user(
            vk_id=self.event.from_id,
            first_name=self.event.from_user.first_name,
            last_name=self.event.from_user.last_name,
        )
