import json

import pytest
from httpx import AsyncClient
from sqlalchemy import insert

from app.config import settings
from app.database import Base, async_session_maker, engine
from app.main import app as fastapi_app
from app.phone_book.models import PhoneBook


@pytest.fixture(scope='session', autouse=True)
async def prepare_database():
    assert settings.MODE == 'TEST'

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(f'app/tests/mock_{model}.json', encoding='utf-8') as file:
            return json.load(file)

    phonebook = open_mock_json('phonebook')

    async with async_session_maker() as session:
        add_phonebook = insert(PhoneBook).values(phonebook)
        await session.execute(add_phonebook)
        await session.commit()


@pytest.fixture(scope='function')
async def ac():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope='function')
async def session():
    async with async_session_maker() as session:
        yield session
