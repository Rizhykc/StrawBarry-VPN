from sqlalchemy import BigInteger, DateTime, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from const import PHONE_LIM, LIMIT


class BaseModel(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now()
    )
    updated: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
    )
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


class Key(BaseModel):
    __tablename__ = 'keys'

    name: Mapped[str] = mapped_column(String(LIMIT), nullable=False)
    key: Mapped[str] = mapped_column(Text)


class User(BaseModel):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    first_name: Mapped[str] = mapped_column(String(LIMIT), nullable=True)
    last_name: Mapped[str] = mapped_column(String(LIMIT), nullable=True)
    phone: Mapped[str] = mapped_column(String(PHONE_LIM), nullable=True)
