# app/db/constant.py
from enum import Enum


class UserRole(Enum):
    OWNER = "owner"
    ADMIN = "admin"
    SELLER = "seller"
    USER = "user"
