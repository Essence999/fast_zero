from pydantic import BaseModel, EmailStr, Field


class Message(BaseModel):
    """A simple message model."""

    message: str


class User(BaseModel):
    """A user model."""

    username: str = Field(pattern=r'^[FTft]\d{7}$')
    password: str = Field(pattern=r'^\d{8}$')
    email: EmailStr


class UserInDB(User):
    """A user model with an additional id field."""

    id: int


class UserPublic(BaseModel):
    """A public user model."""

    id: int
    username: str
    email: EmailStr


class UserList(BaseModel):
    """A list of users model."""

    users: list[UserPublic]
