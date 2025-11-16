import uuid
from typing import Optional

from models.users import User
from pydantic import BaseModel
from sqlmodel import Field, Relationship, SQLModel

"""
info required by a user to log in
identifier is either an email or username
"""


class Login(BaseModel):
    identifier: str
    password: str
    stay_logged_in: Optional[bool] = False


class Session(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    session_id: uuid.UUID = Field(default=None)
    user: User = Relationship(back_populates="active_sessions")
