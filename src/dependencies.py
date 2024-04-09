from typing import Annotated

from fastapi import Body, Depends, HTTPException, Request, status
from openai import OpenAI
from psycopg import Connection

from src.crud import CRUD
from src.genai_features import is_approved, get_violation_reason
from src.models import *


__all__ = [
    'get_conn',
    'get_crud',
    'get_openai_client',
    'message_is_approved',
]


def get_conn(request: Request) -> Connection:
    with request.state.conn_pool.connection() as conn:
        yield conn


def get_crud(conn: Annotated[Connection, Depends(get_conn)]) -> CRUD:
    return CRUD(conn)


def get_openai_client(request: Request) -> OpenAI:
    return request.state.openai_client


def message_is_approved(
        client: Annotated[OpenAI, Depends(get_openai_client)],
        input: Annotated[CommentInput, Body(...)],
) -> None:

    if not is_approved(client, input):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=get_violation_reason(client, input))
