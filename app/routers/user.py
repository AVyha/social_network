from sqlalchemy import select
from fastapi import APIRouter, Depends

from app.auth.database import async_session_maker
from app.auth.utils import current_active_user
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
