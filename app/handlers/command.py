# # app/handlers/command.py
# from aiogram import Router, types
# from aiogram.filters import Command
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import select
# from app.db.models import Command as DemoCommand
# from app.db.error_handler import db_error_handler

# from utils.logger import logger

# router = Router()


# @router.message(Command("list_commands"))
# @db_error_handler()
# async def list_commands_handler(message: types.Message, session: AsyncSession):
#     """
#     List all available commands for the bot.
#     """
#     try:
#         results = await session.execute(select(DemoCommand))
#         commands = [f"/{cmd.command} - {cmd.description}" for cmd in results.scalars()]
#         response = "Available commands:\n" + "\n".join(commands)
#         await message.answer(response)
#     except Exception as e:
#         logger.error(f"Error in commands_handler: {e}")
#         await message.answer("❗ An error occurred while fetching the command list.")


# @router.message(Command("add_command"))
# @db_error_handler()
# async def add_command_handler(message: types.Message, session: AsyncSession):
#     """
#     Add a new command to the database.
#     """
#     try:
#         # Example command syntax: /add_command command_name syntax model_type description
#         parts = message.text.split("|", maxsplit=4)
#         if len(parts) < 4:
#             await message.answer(
#                 "❗ Usage: /add_command <command> <syntax> [description]"
#             )
#             return

#         command_name = parts[1]
#         command = parts[2]
#         related_type = parts[3]
#         description = parts[4] if len(parts) > 4 else ""

#         # Check if command already exists
#         existing_command = await session.scalar(
#             select(DemoCommand).where(DemoCommand.command == command)
#         )
#         if existing_command:
#             await message.answer(f"❗ Command '{command_name}' already exists.")
#             return

#         new_command = DemoCommand(
#             name=command_name,
#             command=command,
#             related_type=related_type,
#             description=description,
#         )
#         session.add(new_command)
#         await session.commit()

#         await message.answer(f"✅ Command '{command_name}' added successfully.")
#     except Exception as e:
#         logger.error(f"Error in add_command_handler: {e}")
#         await message.answer("❗ An error occurred while adding the command.")
