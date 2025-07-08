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


@router.message(Command("profile"))
@db_error_handler()
async def profile_handler(message: types.Message, session: AsyncSession):
    try:
        result = await session.scalar(
            select(User).where(User.telegram_id == message.from_user.id)
        )
        print(f"🚀 {result.__dict__}")
        if not result:
            await message.answer("🚫 You are not registered in the database.")
            return

        response_line = ""
        response_line += f"🥸 ID: {result.telegram_id}\n"
        response_line += (
            f"👤 Username: {result.username if result.username else 'No username'}\n"
        )
        response_line += f"👤 Role: {result.role}\n"
        response_line += f"👤 Created at: {result.created_at}\n"

        await message.answer(response_line)
    except Exception as e:
        logger.error(f"Error in profile_handler: {e}")
        await message.answer("❗ An error occurred while fetching your profile.")
        raise e


@router.message(Command("delete_user"))
@db_error_handler()
async def delete_user(message: types.Message, session: AsyncSession):
    """
    Delete a user by their Telegram ID.
    """
    try:
        user_id = message.text.split()[1] if len(message.text.split()) > 1 else None
        if not user_id:
            await message.answer("❗ Please provide a user ID to delete.")
            return

        user = await session.scalar(
            select(User).where(User.telegram_id == int(user_id))
        )
        if not user:
            await message.answer(f"🚫 User with ID {user_id} not found.")
            return

        await session.delete(user)
        await session.commit()
        await message.answer(f"✅ User with ID {user_id} has been deleted.")
    except Exception as e:
        logger.error(f"Error in delete_user handler: {e}")
        await message.answer("❗ An error occurred while deleting the user.")
        raise e
