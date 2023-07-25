from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class Post(SQLModel, table=True):
    uuid: UUID = Field(
        default_factory=uuid4, primary_key=True, nullable=False, index=True
    )
    user_uuid: UUID = Field(foreign_key="user.uuid", default=None)
    title: str
    description: str
    likes: int
    views: int
