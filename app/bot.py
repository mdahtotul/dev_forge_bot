# app/bot.py

from aiogram import Bot, Dispatcher

from app.config import bot_token
from app.handlers import start, user, command
from app.db.middleware import DBSessionMiddleware, BaseMiddleware


bot = Bot(token=bot_token)
dp = Dispatcher()


# middleware for database session management
dp.message.middleware(DBSessionMiddleware())

# routes for handling commands
dp.include_router(start.router)
dp.include_router(user.router)
# dp.include_router(command.router)
