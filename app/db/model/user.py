# app/db/model/user.py
from sqlalchemy import (
    String,
    DateTime,
    Integer,
    BigInteger,
    Enum as SqlEnum,
    Column,
    func,
)
from sqlalchemy.dialects.postgresql import ENUM as PGEnum
from app.db.base import Base
from app.db.constant import UserRole


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, unique=True, index=True)
    username = Column(String(64), nullable=True)
    phone = Column(String(32), nullable=True)
    role = Column(
        PGEnum(UserRole, name="user_role", create_type=False),
        default=UserRole.USER,
        nullable=False,
    )
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"id: {self.id}, username: {self.username}"
