from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseModel(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now()
    )
    updated: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
    )


class Subscription(BaseModel):
    __tablename__ = 'subscription'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text)


class Proxi(BaseModel):
    __tablename__ = 'proxi'

    id: Mapped[int]
    name: Mapped[str]
    file: Mapped[int]
