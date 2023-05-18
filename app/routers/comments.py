from fastapi import APIRouter, Depends

from app.auth.database import async_session_maker
from app.auth.utils import current_active_user
from app.models import User
from app.models.post import post_comments

router = APIRouter(
    prefix="/post/comments",
    tags=["posts"]
)


@router.get("/view/{post_id}")
async def get_comments(post_id: int, user: User = Depends(current_active_user)):
    query = post_comments.select().where(post_comments.c.post_id == post_id)

    async with async_session_maker() as session:
        response = await session.execute(query)

    comment = [{comment.username: comment.text} for comment in response.fetchall()]

    if not comment:
        return {"status code": 200}

    return {"status code": 200, "comments": comment}


@router.post("/add/{post_id}")
async def add_comment(post_id: int, text: str, user: User = Depends(current_active_user)):
    query = post_comments.insert().values(
        post_id=post_id,
        user_id=user.id,
        text=text,
        username=user.username
    )

    async with async_session_maker() as session:
        await session.execute(query)
        await session.commit()

    return {"status code": 201}
