from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.models import Key


async def orm_add_key(session: AsyncSession, data: dict):
    """Добавление ключа в базу данных."""
    obj = Key(
        name=data['name'],
        key=data['key'],
    )
    session.add(obj)
    await session.commit()


async def get_all_keys(session: AsyncSession):
    """Вывод всех ключей из одной страны в базе данных."""
    result = await session.execute(select(Key))
    return result.scalars().all()


async def orm_get_key(session: AsyncSession, key_id: int):
    """Вывод отдельного ключа из базы данных."""
    query = select(Key).where(Key.id == key_id)
    result = await session.execute(query)
    return result.scalar()


async def orm_delete_key(session: AsyncSession, key_id: int):
    """Удаление ключа из базы данных."""
    query = delete(Key).where(Key.id == key_id)
    await session.execute(query)
    await session.commit()


async def orm_update_key(
    session: AsyncSession,
    key_id: int, data
):
    """Обновление ключа в базе данных."""
    query = update(Key).where(Key.id == key_id).values(
        name=data['name'],
    )
    await session.execute(query)
    await session.commit()
