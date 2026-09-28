from pydantic import BaseModel
from datetime import datetime
from app.models.incident import IncidentStatus

class IncidentCreate(BaseModel):
    repository: str
    commit_id : str
    build_id : int

class IncidentResponse(BaseModel):
    id : int
    repository: str
    commit_id : str
    build_id : int
    status : IncidentStatus
    created_at : datetime

    class Config:
        from_attributes = True

class IncidentStatusUpdate(BaseModel):
    status : IncidentStatus

