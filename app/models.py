import uuid
from app.database import Base
from sqlalchemy import Column, String, JSON
from sqlalchemy.dialects.postgresql import UUID


class TaskModel(Base):
    __tablename__ = 'task'

    task_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    description = Column(String, nullable=False)
    params = Column(JSON, nullable=False)
