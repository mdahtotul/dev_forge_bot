# app/db/error_handler.py
from functools import wraps
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
import logging
from aiogram.types import Message

logger = logging.getLogger(__name__)


def db_error_handler():
    def decorator(func):
        @wraps(func)
        async def wrapper(message: Message, session: AsyncSession, *args, **kwargs):
            try:
                return await func(message, session, *args, **kwargs)
            except SQLAlchemyError as e:
                await session.rollback()
                # Log full traceback
                logger.exception("❌ Database error in handler:")

                # Show clean message to user
                await message.answer(
                    "⚠️ An internal database error occurred. Please try again later."
                )

        return wrapper

    return decorator
