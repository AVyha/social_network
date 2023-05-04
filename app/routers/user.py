from sqlalchemy import select, insert, delete
from fastapi import APIRouter, Depends

from app.auth.database import async_session_maker
from app.auth.utils import current_active_user
from app.models import Follow
from app.models.user import User

router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.get("/me")
def get_user_page(user: User = Depends(current_active_user)):
    return {"status code": 200, "username": user.username}


@router.get("/{username}", dependencies=[Depends(current_active_user)])
async def get_user_by_username(username: str):
    query = select(User).where(User.username == username)

    async with async_session_maker() as session:
        response = await session.execute(query)

    try:
        user = response.fetchone()[0].username
    except TypeError:
        return {"status code": 404}

    return {"status code": 200, "username": user}


@router.get("/follow/{username}")
async def follow_to_user(username: str, user: User = Depends(current_active_user)):
    query = select(User).where(
        User.username == username
    )

    async with async_session_maker() as session:
        response = await session.execute(query)

        user_to_follow = response.fetchone()[0]

        if user_to_follow is None or user_to_follow.id == user.id:
            return {"status code": 404}

    query = select(Follow).where(
        Follow.user_id == user.id,
        Follow.follower_id == user_to_follow.id
    )

    async with async_session_maker() as session:
        response = await session.execute(query)

        result = response.first()

        if result is None:
            follow = insert(Follow).values(
                user_id=user.id,
                follower_id=user_to_follow.id
            )
            status = 200
        else:
            follow = delete(Follow).where(
                Follow.user_id == user.id,
                Follow.follower_id == user_to_follow.id
            )
            status = 204

        await session.execute(follow)
        await session.commit()

    return {"status code": status}

