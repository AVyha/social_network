import uuid

import uvicorn
from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from app.auth.auth import auth_backend
from app.auth.manager import get_user_manager
from app.schemas.auth import UserRead, UserCreate
from auth.database import User

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

app = FastAPI()

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


@app.get("/")
def index():
    return {"status code": 200}


if __name__ == "__main__":
    uvicorn.run("main:app")
