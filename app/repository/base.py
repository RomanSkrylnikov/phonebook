from sqlalchemy import insert, select

from app.database import async_session_maker


class BaseRepo:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(id=model_id)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(cls, **kwargs):
        async with async_session_maker() as session:
            query = (
                select(cls.model.__table__.columns)
                .filter_by(**kwargs)
                .order_by(cls.model.id)
            )
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update_object(cls, update_data, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**kwargs)
            result = await session.execute(query)
            result = result.scalar_one_or_none()
            new_data = update_data.dict(exclude_unset=True)
            for key, value in new_data.items():
                setattr(result, key, value)
            session.add(result)
            await session.commit()

    @classmethod
    async def delete_object(cls, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**kwargs)
            result = await session.execute(query)
            result = result.scalar_one_or_none()
            await session.delete(result)
            await session.commit()
