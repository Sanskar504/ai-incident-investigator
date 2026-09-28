from pydantic import BaseModel
from datetime import datetime

class InvestigationCreate(BaseModel):
    probable_cause: str
    evidence : str
    confidence : float
    probable_solution : str

class InvestigationResponse(BaseModel):
    id : int
    incident_id : int
    probable_cause : str
    evidence : str
    confidence : float
    probable_solution : str
    
    class Config:
        from_attributes = True