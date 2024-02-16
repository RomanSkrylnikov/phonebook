from typing import Optional

from pydantic import BaseModel, ConfigDict


class SPhoneBook(BaseModel):
    """Базовая модель пользователя"""

    id: int
    lastname: str
    name: str
    middlename: Optional[str] = None
    org_name: Optional[str] = None
    work_phone: Optional[str] = None
    cell_phone: str

    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    """Модель для создания нового пользователя"""

    lastname: str
    name: str
    middlename: Optional[str] = None
    org_name: Optional[str] = None
    work_phone: Optional[str] = None
    cell_phone: str

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    """Модель для обновления данных пользователя"""

    lastname: Optional[str] = None
    name: Optional[str] = None
    middlename: Optional[str] = None
    org_name: Optional[str] = None
    work_phone: Optional[str] = None
    cell_phone: Optional[str] = None
