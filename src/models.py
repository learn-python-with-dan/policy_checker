from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, computed_field


__all__ = [
    'Comment',
    'CommentInput',
]


class Comment(BaseModel):
    id: UUID
    content: str
    created_at: datetime


class CommentInput(BaseModel):
    content: str

    @computed_field
    @property
    def id(self) -> UUID:
        return uuid4()

    @computed_field
    @property
    def created_at(self) -> datetime:
        return datetime.now()
