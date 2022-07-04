from pydantic import BaseModel
from uuid import UUID


class PostCreate(BaseModel):
    title: str
    description: str
    price: float
    trade: bool
    uuid: UUID
    class Config:
        orm_mode = True

class PostCreateRequest(BaseModel):
    title: str
    description: str
    price: float
    trade: bool
    class Config:
        orm_mode = True

# class Post(Base):
#     __tablename__ = "posts"
#     __table_args__ = {"schema": "public"}
#     id = Column("id", BigInteger, primary_key=True, index=True, autoincrement=True, unique=True, nullable=False)
#     uuid = Column("uuid", UUID(as_uuid=True), primary_key=True, unique=True, nullable=False)
#     userId = Column("user_id", BigInteger, ForeignKey("public.users.id"), nullable=False)
#     title = Column("title", String, nullable=False)
#     description = Column("description", String, nullable=False)
#     price = Column("price", Float)
#     trade = Column("trade", BOOLEAN, nullable=False)
#
#     photos = relationship("PostPhoto", back_populates="owner")
#     user = relationship("User", back_populates="posts")


