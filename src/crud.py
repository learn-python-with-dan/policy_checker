from typing import TypeVar
from uuid import UUID

from psycopg import Connection
from psycopg.rows import class_row
from pydantic import BaseModel

from src.models import *
from src.statements import *


__all__ = [
    'CRUD'
]


T = TypeVar('T')


class CRUD:

    def __init__(self, conn: Connection):
        self.conn = conn

    def _insert_resource(self, stmt: str, input: BaseModel) -> UUID:
        with self.conn.cursor() as cursor:
            cursor.execute(stmt, input.model_dump())
            return cursor.fetchone()[0]

    def _get_resource(self, stmt: str, model_class: type[T], **kwargs) -> T | None:
        with self.conn.cursor(row_factory=class_row(model_class)) as cursor:
            cursor.execute(stmt, kwargs)
            return cursor.fetchone()

    def insert_comment(self, input: CommentInput) -> UUID:
        return self._insert_resource(insert_comment_stmt, input)

    def get_comment(self, id: UUID) -> Comment | None:
        return self._get_resource(get_comment_stmt, Comment, id=id)
