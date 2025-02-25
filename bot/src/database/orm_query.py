from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Subscription as Sub


async def orm_add_subscription(session: AsyncSession, data: dict):
    obj = Sub(
        name=data['name'],
        description=data['description'],
    )
    session.add(obj)
    await session.commit()


async def orm_get_subscriptions(session: AsyncSession):
    query = select(Sub)
    result = await session.execute(query)
    return result.scalars().all()


async def orm_get_subscription(session: AsyncSession, product_id: int):
    query = select(Sub).where(Sub.id == product_id)
    result = await session.execute(query)
    return result.scalar()


async def orm_update_subscription(
    session: AsyncSession,
    product_id: int, data
):
    query = update(Sub).where(Sub.id == product_id).values(
        name=data['name'],
        description=data['description'],
    )
    await session.execute(query)
    await session.commit()


async def orm_delete_subscription(session: AsyncSession, product_id: int):
    query = delete(Sub).where(Sub.id == product_id)
    await session.execute(query)
    await session.commit()
