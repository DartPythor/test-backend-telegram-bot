from datetime import datetime
from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional

class CustomUserCreate(BaseModel):
    telegram_id: int = Field(..., description="Telegram ID пользователя")
    username: Optional[str] = None
    password: str

class CustomUserResponse(BaseModel):
    telegram_id: int
    username: str
    email: str | None
    first_name: str | None
    last_name: str | None

class TaskCreate(BaseModel):
    title: str = Field(..., max_length=200)
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    tags: List[str] = []
    user: int

class TaskResponse(BaseModel):
    task_id: str
    user: int
    title: str
    due_date: datetime
    tags: list[str]


class CategoryCreate(BaseModel):
    name: str = Field(..., max_length=100)
    user: int

class CategoryResponse(CategoryCreate):
    category_id: str

