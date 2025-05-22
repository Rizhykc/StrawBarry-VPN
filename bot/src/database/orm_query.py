from typing import Union

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.engine import session_maker
from src.database.models import Country, Key


async def orm_add_country(session: AsyncSession, data: dict):
    """Добавление страны в базу данных."""
    obj = Country(
        name=data['name'],
    )
    session.add(obj)
    await session.commit()


async def orm_get_countries(session: Union[AsyncSession, None] = None):
    """Вывод всех стран из базы данных."""
    query = select(Country)
    if session is not None:
        result = await session.execute(query)
        return result.scalars().all()
    async with session_maker() as sess:
        return await sess.scalars(query)


async def orm_get_country(session: AsyncSession, country_id: int):
    """Вывод отдельной страны из базы данных."""
    query = select(Country).where(Country.id == country_id)
    result = await session.execute(query)
    return result.scalar()


async def orm_update_country(
    session: AsyncSession,
    country_id: int, data
):
    """Обновление страны в базе данных."""
    query = update(Country).where(Country.id == country_id).values(
        name=data['name'],
    )
    await session.execute(query)
    await session.commit()


async def orm_delete_country(session: AsyncSession, country_id: int):
    """Удаление страны из базы данных."""
    query = delete(Country).where(Country.id == country_id)
    await session.execute(query)
    await session.commit()


async def orm_add_key(session: AsyncSession, data: dict):
    """Добавление страны в базу данных."""
    obj = Key(
        name=data['name'],
        key=data['key'],
        country=data['countries_id'],
    )
    session.add(obj)
    await session.commit()


async def orm_get_keys(session: AsyncSession, country_id: int):
    """Вывод всех ключей из одной страны в базе данных."""
    query = select(Key).where(Key.country == country_id)
    result = await session.execute(query)
    return result.scalar()


async def orm_get_key(session: AsyncSession, key_id: int):
    query = select(Key).where(Key.id == key_id)
    result = await session.execute(query)
    return result.scalar()
