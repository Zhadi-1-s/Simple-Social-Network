import uuid as uuid_pkg
from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine

DB_FILE = "db.sqlite3"
engine = create_engine(f"sqlite:///{DB_FILE}", echo=True)


async def get_session():
    with Session(engine) as session:
        yield session


class PostModel(SQLModel, table=True):
    uuid: Optional[uuid_pkg.UUID] = Field(
        default_factory=uuid_pkg.uuid4, primary_key=True, nullable=False, index=True
    )
    user_uuid: uuid_pkg.UUID = Field(default=None)
    title: str
    description: str
    likes: int
    views: int


def create_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_tables()
