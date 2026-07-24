from vkbottle.bot import Message

from config import Bot
from logger import logger

from .labeler import labeler

from database.invites import (
    get_active_invites,
    get_invite,
    approve_invite,
    reject_invite,
)

from database.states import (
    get_state,
    set_state,
    clear_state,
)

from modules.invite.states import InviteState


@labeler.message()
async def invite_handler(message: Message):
    payload = message.get_payload_json()

    if not payload:
        return
    # Обработка кнопок
    else:
        cmd = payload.get("cmd")

        match cmd:

            case "invite_komsenok":
                logger.info("Into invite_komsenok")

                invite = await get_active_invites(message.from_id)

                if invite:
                    await message.answer(
                        "У вас уже есть необработанная заявка."
                    )
                    return

                await set_state(
                    message.from_id,
                    InviteState.WAIT_BLOCK
                )

                await message.answer(
                    "Введите номер блока."
                )


            case "approve_invite":
                invite_id = payload["invite"]

                await approve_invite(
                    invite_id=invite_id,
                    admin_vk=message.from_id,
                )

                invite = await get_invite(invite_id)

                await Bot.api.messages.send(
                    peer_id=invite.student_vk,
                    random_id=0,
                    message=(
                        f"✅ Воспитатель одобрил приглашение "
                        f"в {invite.block} блок.\n"
                        "Ждем ответа от комсенка"
                    )
                )


            case "reject_invite":
                invite_id = payload["invite"]

                await reject_invite(
                    invite_id=invite_id,
                    admin_vk=message.from_id,
                )

                invite = await get_invite(invite_id)

                await Bot.api.messages.send(
                    peer_id=invite.student_vk,
                    random_id=0,
                    message="❌ Воспитатель отклонил приглашение."
                )


    # Обработка состояний
    state = await get_state(message.from_id)

    if state is None:
        return

    match state:

        case InviteState.WAIT_BLOCK:
            block = message.text.strip()

            await create_invite(
                student_vk=message.from_id,
                block=block,
            )

            await clear_state(message.from_id)

            await message.answer(
                f"Заявка на приглашение в {block} блок создана."
            )