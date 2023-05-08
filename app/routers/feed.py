from fastapi import APIRouter, Depends
from sqlalchemy import select, or_

from app.auth.database import async_session_maker
from app.auth.utils import current_active_user
from app.models import Follow, Post
from app.models.user import User

router = APIRouter(
    prefix="/feed",
    tags=["feed"]
)


@router.get("/")
async def get_feed(user: User = Depends(current_active_user)):
    query = select(Follow.follower_id).where(Follow.user_id == user.id)

    async with async_session_maker() as session:
        response = await session.execute(query)

        all_follows = response.fetchall()

        follows_username = [follow.follower_id for follow in all_follows]

        condition = or_(Post.author_id.in_(follows_username))

        query = select(Post.text).where(condition)

        response = await session.execute(query)

        feed = response.fetchall()

    result = [i.text for i in feed]

    return {"status code": 200, "feed": result}
