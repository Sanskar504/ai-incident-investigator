from pydantic import BaseModel
from datetime import datetime

class EvidenceCreate(BaseModel):
    source : str
    content : str
    timestamp : datetime
    message : str
    severity : str



class EvidenceResponse(BaseModel):
    id : int
    incident_id : int
    timestamp : datetime
    message : str
    severity : str
    source : str
    content : str
    created_at : datetime
    
