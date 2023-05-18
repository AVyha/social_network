import uvicorn
from fastapi import FastAPI, Depends

from app.auth.auth import auth_backend
from app.auth.utils import fastapi_users, current_active_user
from app.schemas.auth import UserRead, UserCreate

from app.routers.user import router as user_router
from app.routers.post import router as post_router
from app.routers.feed import router as feed_router
from app.routers.comments import router as comment_router
from app.routers.message import router as message_router

app = FastAPI()

app.include_router(
    user_router
)

app.include_router(
    post_router
)

app.include_router(
    feed_router
)

app.include_router(
    comment_router
)

app.include_router(
    message_router
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


@app.get("/", dependencies=[Depends(current_active_user)])
def index():
    return {"status code": 200}


if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True, host="0.0.0.0", port=8000)
