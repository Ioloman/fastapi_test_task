from typing import Union
from uuid import UUID
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database import get_db
from api.schemas import Task, TaskCreate, TaskBase
import api.crud as crud

app = FastAPI()


@app.post('/tasks/add', response_model=Task)
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)


@app.get('/tasks', response_model=list[Task])
async def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)


@app.put('/tasks/{task_id}', response_model=Task)
async def update_task(task_id: UUID, task: Union[Task, TaskBase], db: Session = Depends(get_db)):
    # to enable both: with and without task_uuid in the body
    if not (isinstance(task, Task)):
        task = Task(task_uuid=task_id, **task.dict())

    # process id mistake
    if task_id != task.task_uuid:
        raise HTTPException(status_code=400, detail='url and body uuids are different')

    return crud.update_task(db, task)


