from typing import List

from fastapi import APIRouter

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
)


@router.get("/")
async def get_posts():
    pass


@router.get("/{post_UUID}")
async def get_post(post_UUID: str):
    pass


@router.post("/")
async def create_post(post_data):
    pass


@router.delete("/{post_UUID}")
def delete_post(post_UUID: str):
    pass
