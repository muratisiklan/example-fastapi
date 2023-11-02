from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    # This might not needed in mysql ????? or mybe sqlalchemy version 2
    #  doesnt need while version 1.4 needs. maybe about pydantic???
    class Config:
        from_attributes = True


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    # Define response structure whith defining types and fields
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse

    # This might not needed in mysql ????? or mybe sqlalchemy version 2 doesnt need while version 1.4 needs
    # maybe about pydantic???
    class Config:
        from_attributes = True


class PostOut(PostBase):
    Post: PostResponse
    votes: int

    class Config:
        from_attributes = True
    title: Optional[str] = None
    content: Optional[str] = None


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
