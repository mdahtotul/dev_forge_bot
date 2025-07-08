# app/db/models.py
from sqlalchemy import (
    String,
    DateTime,
    Integer,
    BigInteger,
    Enum as SqlEnum,
    Column,
    func,
)
from app.db.base import Base
from app.db.constant import UserRole


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, unique=True, index=True)
    username = Column(String(64), nullable=True)
    role = Column(SqlEnum(UserRole), default=UserRole.USER, nullable=False)
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"id: {self.id}, username: {self.username}"

    # id: Mapped[int] = mapped_column(primary_key=True)
    # telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True)
    # username: Mapped[str] = mapped_column(String(64), nullable=True)
    # role: Mapped[UserRole] = mapped_column(
    #     SqlEnum(UserRole), default=UserRole.USER, nullable=False
    # )
