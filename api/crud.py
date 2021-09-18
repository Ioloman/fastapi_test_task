from fastapi import HTTPException
from sqlalchemy.orm import Session
import api.models as models
import api.schemas as schemas


def get_tasks(db: Session) -> list[models.TaskModel]:
    """
    Returns all tasks from database
    """
    return db.query(models.TaskModel).all()


def create_task(db: Session, task: schemas.TaskCreate) -> models.TaskModel:
    """
    Adds task to database
    """
    db_task = models.TaskModel(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: Session, task: schemas.Task) -> models.TaskModel:
    """
    Updates task
    """
    db_task: models.TaskModel = db.query(models.TaskModel).get(task.task_uuid)

    # to return 404 if task wasn't found
    if db_task is None:
        raise HTTPException(status_code=404, detail='Task not found')

    db_task.description = task.description
    db_task.params = task.params.dict()
    db.commit()
    return db_task
