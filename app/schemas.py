from uuid import UUID
from pydantic import BaseModel


class Params(BaseModel):
    param_1: str
    param_2: int


class Task(BaseModel):
    task_uuid: UUID
    description: str
    params: Params


class TaskIn(BaseModel):
    description: str
    params: Params
