from typing import Annotated

from fastapi import APIRouter, Body, Depends, status

from src.crud import CRUD
from src.dependencies import *
from src.models import *


__all__ = [
    'router',
]


router = APIRouter(
    tags=['Comments'],
    prefix='/comments',
)


@router.post(path='', response_model=Comment, status_code=status.HTTP_201_CREATED, dependencies=[Depends(message_is_approved)])
def create_user(
        crud: Annotated[CRUD, Depends(get_crud)],
        input: Annotated[CommentInput, Body(...)],
) -> Comment:
    comment_id = crud.insert_comment(input)
    return crud.get_comment(comment_id)
