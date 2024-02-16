from fastapi import FastAPI

from app.phone_book.router import router as phone_book_router

app = FastAPI(title='PhoneBook')

app.include_router(phone_book_router)
