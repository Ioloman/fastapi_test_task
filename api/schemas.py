from uuid import UUID
from pydantic import BaseModel


class Params(BaseModel):
    param_1: str
    param_2: int


class TaskBase(BaseModel):
    description: str
    params: Params


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    task_uuid: UUID

    class Config:
        orm_mode = True
