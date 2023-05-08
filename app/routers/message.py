from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert

from app.auth.database import async_session_maker
from app.auth.utils import current_active_user
from app.models import User, Message

router = APIRouter(
    prefix="/messages",
    tags=["message"]
)


@router.post("/")
async def send_message(receiver_uuid: UUID, message: str, user: User = Depends(current_active_user)):
    query = insert(Message).values(
        message=message,
        from_user=user.id,
        to_user=receiver_uuid
    )

    async with async_session_maker() as session:
        await session.execute(query)
        await session.commit()

    return {"status code": 200}


@router.get("/")
async def get_messages(second_user_uuid: UUID, user: User = Depends(current_active_user)):
    first_user_query = select(Message).where(
        Message.from_user == user.id,
        Message.to_user == second_user_uuid
    )

    second_user_query = select(Message).where(
        Message.from_user == second_user_uuid,
        Message.to_user == user.id
    )

    async with async_session_maker() as session:
        first_user_response = await session.execute(first_user_query)
        second_user_response = await session.execute(second_user_query)

    messages_from_first_user = [
        {
            "time": message[0].time,
            "message": message[0].message,
            "from": message[0].from_user
        }
        for message in first_user_response.fetchall()
    ]

    messages_from_second_user = [
        {
            "time": message[0].time,
            "message": message[0].message,
            "from": message[0].from_user
        }
        for message in second_user_response.fetchall()
    ]

    return {
        "status code": 200,
        "first_user_messages": messages_from_first_user,
        "second_user_messages": messages_from_second_user
    }
