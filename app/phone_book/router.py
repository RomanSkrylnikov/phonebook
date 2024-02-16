from typing import List, Optional

from fastapi import APIRouter, Depends

from app.phone_book.repo import BookRepo
from app.phone_book.schemas import SPhoneBook, UserCreate, UserUpdate

router = APIRouter(prefix="/phone_book", tags=["Справочник"])


@router.get("", response_model=List[SPhoneBook])
async def find_all_users():
    """Возвращает всех пользователей"""
    users = await BookRepo.find_all()
    return users


@router.get("/{user_id}", response_model=SPhoneBook)
async def find_user_by_id(user_id: int):
    """Возвращает конкретного пользователя"""
    user = await BookRepo.find_by_id(model_id=user_id)
    return user


@router.post("/{phone_number}")
async def find_by_phone_number(phone_number: str):
    """Находит пользователя по номеру телефона"""
    user = await BookRepo.find_by_phone_number(phone_cell=phone_number)
    return user


@router.post("/")
async def find_by_name(lastname: str, name: str, middlename: Optional[str] = None):
    """Находит пользователя по ФИО"""
    user = await BookRepo.find_by_fio(
        lastname=lastname, name=name, middlename=middlename
    )
    return user


@router.post("")
async def create_user(data: UserCreate = Depends(UserCreate)):
    """Создает нового пользователя"""
    new_user = await BookRepo.add(**data.model_dump())

    return new_user


@router.patch("/{user_id}")
async def update_data(user_id: int, update_data: UserUpdate = Depends(UserCreate)):
    """Изменяет данные пользователя"""
    user = await BookRepo.update_object(update_data=update_data, id=user_id)
    return user


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    """Удаляет пользователя"""
    result = await BookRepo.delete_object(id=user_id)

    return result
