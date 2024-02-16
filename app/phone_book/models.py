from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class PhoneBook(Base):
    """Модель данных для телефонного справочника"""

    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True)
    lastname: Mapped[str]
    name: Mapped[str]
    middlename: Mapped[Optional[str]]
    org_name: Mapped[Optional[str]]
    work_phone: Mapped[Optional[str]]
    cell_phone: Mapped[str]
