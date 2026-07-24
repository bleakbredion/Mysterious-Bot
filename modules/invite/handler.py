from vkbottle.bot import Message

from config import Bot
from logger import logger

from .labeler import labeler

from database.invites import (
    get_active_invites,
    get_invite,
    create_invite,
    approve_invite,
    reject_invite,
)

from database.states import (
    get_state,
    set_state,
    clear_state,
)

from modules.invite.states import InviteState


# ==========================================================
# Кнопки
# ==========================================================

@labeler.message(payload={"cmd": "invite_komsenok"})
async def invite_start(message: Message):

    invite = await get_active_invites(message.from_id)

    if invite:
        await message.answer("У вас уже есть необработанная заявка.")
        return

    await set_state(message.from_id, InviteState.WAIT_BLOCK)

    await message.answer(
        "Введите номер блока."
    )


@labeler.message(payload={"cmd": "approve_invite"})
async def approve(message: Message):
    payload = message.get_payload_json()

    invite_id = payload["invite"]

    await approve_invite(
        invite_id=invite_id,
        admin_vk=message.from_id,
    )

    invite = await get_invite(invite_id)

    await Bot.api.messages.send(
        peer_id=invite.student_vk,
        random_id=0,
        message=f"✅ Воспитатель одобрил приглашение в {invite.block} блок.\nЖдем ответа от комсенка"
    )


@labeler.message(payload={"cmd": "reject_invite"})
async def reject(message: Message):
    payload = message.get_payload_json()

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


# ==========================================================
# Состояния
# ==========================================================

@labeler.message()
async def invite_state(message: Message):
    state = await get_state(message.from_id)

    if state is None:
        return

    match state:

        case InviteState.WAIT_BLOCK:
            pass