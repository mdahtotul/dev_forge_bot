# app/db/model/command.py
from sqlalchemy import (
    String,
    DateTime,
    Integer,
    BigInteger,
    Enum as SqlEnum,
    Column,
    Boolean,
    func,
)
from app.db.base import Base


class TgCommand(Base):
    __tablename__ = "tg_commands"

    id = Column(Integer, primary_key=True)
    name = Column(String(256), unique=True, nullable=False)
    command = Column(String(1000), nullable=False)
    description = Column(String(1000), nullable=True)
    is_public = Column(Boolean, default=True)
    priority = Column(Integer, default=1)
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"name: {self.name}, command: {self.command}"
