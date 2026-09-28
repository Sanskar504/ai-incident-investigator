from pydantic import BaseModel
from datetime import datetime

class EvidenceCreate(BaseModel):
    source : str
    content : str


class EvidenceResponse(BaseModel):
    id : int
    incident_id : int
    source : str
    content : str
    created_at : datetime
    
