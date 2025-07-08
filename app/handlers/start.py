# app/handlers/start.py
from aiogram import Router, types, F
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import User

router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message, session: AsyncSession):
    user = await session.scalar(
        User.__table__.select().where(User.telegram_id == message.from_user.id)
    )
    if not user:
        session.add(
            User(telegram_id=message.from_user.id, username=message.from_user.username)
        )
        await session.commit()
        await message.answer("👋 Welcome! You have been added.")
    else:
        await message.answer("👋 Welcome back!")
