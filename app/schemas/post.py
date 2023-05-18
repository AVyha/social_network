from pydantic import BaseModel


class CreatePost(BaseModel):
    text: str
    # file: bytes
