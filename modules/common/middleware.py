from vkbottle.dispatch.middlewares import BaseMiddleware

from modules.common.create_or_update_user import create_or_update_user


class UserMiddleware(BaseMiddleware):
    async def pre(self):
        await create_or_update_user(
            vk_id=self.event.from_id,
            first_name=self.event.from_user.first_name,
            last_name=self.event.from_user.last_name,
        )
