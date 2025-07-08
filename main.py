# main.py
import asyncio
from app.bot import bot, dp
from app.db.base import Base
from app.db.session import engine


async def main():
    # Create DB tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print("🤖 Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
