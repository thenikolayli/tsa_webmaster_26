from datetime import datetime, timezone
from typing import Optional

from models.auth import Session
from passlib.hash import argon2
from pydantic import BaseModel
from sqlmodel import Field, Relationship, SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    roles: list[str] = Field(default_factory=list)
    created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    active_sessions: list[Session] = Relationship(back_populates="user")

    # hashes the password
    def hash_password(self):
        self.password = argon2.hash(self.password)

    # compares a plaintext password to the hashed password
    def verify_password(self, password):
        return argon2.verify(password, self.password)


# schema for creating a user
class CreateUser(BaseModel):
    email: str
    username: str
    password: str
