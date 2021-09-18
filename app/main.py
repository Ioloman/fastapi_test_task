from uuid import UUID, uuid1
from fastapi import FastAPI
from app.schemas import Task, TaskIn

app = FastAPI()

db: list[Task] = []


@app.post('/tasks/add')
async def add_task(task: TaskIn):
    global db
    new_task = Task(task_uuid=uuid1(), **task.dict())
    db.append(new_task)
    return {'status': 'success', 'data': new_task}


@app.get('/tasks')
async def get_tasks():
    return {'status': 'success', 'data': db}


@app.put('/tasks/{task_id}')
async def update_task(task_id: UUID, task: TaskIn):
    global db
    for i in range(len(db)):
        if db[i].task_uuid == task_id:
            db[i] = Task(task_uuid=task_id, **task.dict())
            return {'status': 'success', 'data': db[i]}
    else:
        return {
            'status': 'error',
            'message': 'Item does not exist',
        }


