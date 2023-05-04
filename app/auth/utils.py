import uuid

from fastapi_users import FastAPIUsers

from app.auth.auth import auth_backend
from app.auth.database import User
from app.auth.manager import get_user_manager

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

current_active_user = fastapi_users.current_user(active=True)
