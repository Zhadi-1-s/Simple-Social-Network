from typing import Union
from uuid import UUID

from fastapi import APIRouter, Depends, Response
from sqlmodel import Session, select

from core import models
from service import database

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
)


@router.get("/")
async def get_posts(session: Session = Depends(database.get_session)):
    stmt = select(database.PostModel)
    posts = session.exec(stmt).all()
    return posts


@router.get("/{post_UUID}", response_model=Union[models.Post, str])
async def get_post(
    post_UUID: UUID,
    response: Response,
    session: Session = Depends(database.get_session),
):
    post = session.get(database.PostModel, post_UUID)
    if post is None:
        response.status_code = 404
        return "Post not found"
    return post


@router.post("/", response_model=models.Post, status_code=201)
async def create_post(
    post: database.PostModel, session: Session = Depends(database.get_session)
):
    session.add(post)
    session.commit()
    session.refresh(post)
    return post


@router.put("/{post_UUID}", response_model=Union[models.Post, str])
async def update_post(
    post_UUID: UUID,
    updated_post: models.Post,
    response: Response,
    session: Session = Depends(database.get_session),
):
    current_post = session.get(database.PostModel, post_UUID)

    if current_post is None:
        # Case when there's no post with post_UUID
        response.status_code = 404
        return "Post not found"

    # Updating post data
    new_post_dict = updated_post.dict(exclude_unset=True)
    for key, val in new_post_dict.items():
        setattr(current_post, key, val)

    session.add(current_post)
    session.commit()
    session.refresh(current_post)
    return current_post


@router.delete("/{post_UUID}")
def delete_post(
    post_UUID: str,
    response: Response,
    session: Session = Depends(database.get_session),
):
    post = session.get(database.PostModel, post_UUID)

    if post is None:
        # Case when there's no post with post_UUID
        response.status_code = 404
        return "Post not found"

    session.delete(post)
    session.commit()

    return Response(status_code=200)
