from fastapi import APIRouter, Depends
from sqlalchemy import select, insert

from app.auth.database import async_session_maker
from app.auth.utils import current_active_user
from app.models.post import Post, post_details
from app.models.user import User
from app.schemas.post import CreatePost

router = APIRouter(
    prefix="/post",
    tags=["posts"]
)


@router.post("/create")
async def create_post(text: CreatePost, user: User = Depends(current_active_user)):
    query = insert(Post).values(text=text.text, author=user.username)

    async with async_session_maker() as session:
        await session.execute(query)
        await session.commit()

    return {"status code": 201, "text": text}


@router.get("/{post_id}")
async def get_post(post_id: int, user: User = Depends(current_active_user)):
    query = select(Post).where(Post.id == post_id)

    async with async_session_maker() as session:
        response = await session.execute(query)

    post = response.first()

    if post is None:
        return {"status code": 404}

    return {"status code": 200, "text": post[0].text}


@router.get("/like/{post_id}")
async def like_post(post_id: int, user: User = Depends(current_active_user)):
    query = post_details.select().where(
        post_details.c.post_id == post_id,
        post_details.c.user_id == user.id
    )

    async with async_session_maker() as session:
        response = await session.execute(query)

        like = response.fetchone()

        if like is None:
            like = post_details.insert().values(
                post_id=post_id,
                user_id=user.id
            )
            status = 200
        else:
            like = post_details.delete().where(
                post_details.c.post_id == post_id,
                post_details.c.user_id == user.id
            )
            status = 204

        await session.execute(like)
        await session.commit()

    return {"status code": status}
