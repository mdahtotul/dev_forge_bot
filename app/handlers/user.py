# app/handlers/user.py
from aiogram import Router, types
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models import User
from app.db.error_handler import db_error_handler

from utils.logger import logger

router = Router()


@router.message(Command("list_users"))
@db_error_handler()
async def list_users(message: types.Message, session: AsyncSession):
    """
    List all users in the database.
    """
    try:
        result = await session.execute(select(User))
        users = result.scalars().all()
        if not users:
            await message.answer("🚫 No users found.")
            return

        response_lines = ""
        print(f"🚀 Users found: {len(users)}")
        for user in users:
            username = user.username if user.username else "No username"
            id = user.telegram_id
            response_lines += f"🥸 ID: {id}, Username: {username}\n"

        await message.answer("👥 List of users:\n" + response_lines)
    except Exception as e:
        logger.error(f"Error in list_users handler: {e}")
        await message.answer("❗ An error occurred while fetching the user list.")
