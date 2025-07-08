# app/bot.py
from aiogram import Bot, Dispatcher
from app.config import bot_token
from app.handlers import start, user
from app.db.middleware import DBSessionMiddleware

bot = Bot(token=bot_token)
dp = Dispatcher()

dp.message.middleware(DBSessionMiddleware())
dp.include_router(start.router)
dp.include_router(user.router)
