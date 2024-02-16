from typing import Optional

from sqlalchemy import and_, select

from app.database import async_session_maker
from app.phone_book.models import PhoneBook
from app.repository.base import BaseRepo


class BookRepo(BaseRepo):
    model = PhoneBook

    @classmethod
    async def find_by_phone_number(cls, phone_cell: str):
        """Находит пользователя по номеру телефона"""
        async with async_session_maker() as session:
            query = select(PhoneBook).where(PhoneBook.cell_phone == phone_cell)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_by_fio(
        cls, lastname: str, name: str, middlename: Optional[str] = str
    ):
        """Находит пользователя по ФИО"""
        async with async_session_maker() as session:
            query = select(PhoneBook).where(
                and_(
                    PhoneBook.lastname == lastname,
                    PhoneBook.name == name,
                    PhoneBook.middlename == middlename,
                )
            )
            result = await session.execute(query)
            return result.mappings().all()
