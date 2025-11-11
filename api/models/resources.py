from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

"""
class representing what every resource has
table=True because it also represents services, which don't have any special fields (broad)
"""
class ResourceBase(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    photo_url: Optional[str]
    website_url: str
    tags: list[str] = Field(default_factory=list)

class Place(ResourceBase, table=True):
    address: str

class Event(ResourceBase, table=True):
    start: datetime
    end: datetime