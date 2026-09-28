from fastapi import FastAPI, Depends, HTTPException
from app.database.base import Base 
from app.database.connection import SessionLocal, engine, get_db
from app.models.incident import Incident
from app.schemas.incident import IncidentCreate, IncidentResponse , IncidentStatusUpdate
from sqlalchemy.orm import Session
from app.models.investigation import Investigation
from app.schemas.investigation import InvestigationCreate , InvestigationResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()



@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/incidents",response_model=IncidentResponse)
def create_incident(
    incident: IncidentCreate,
    db: Session = Depends(get_db)
):
    db_incident = Incident(
        repository = incident.repository,
        commit_id = incident.commit_id,
        build_id = incident.build_id
    )

    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident

@app.get("/incidents")
def get_incidents(
    db: Session = Depends(get_db)
):
    incidents = db.query(Incident).all()
    return incidents

@app.get("/incidents/{incident_id}",response_model=IncidentResponse)
def get_incident_by_id(
    incident_id: int,
    db: Session = Depends(get_db)
):
    incident = db.query(Incident).filter(
        Incident.id==incident_id
        ).first()

    if incident is None:
        raise HTTPException(
        status_code=404,
        detail="Incident not found"
)
    return incident                                   
    

@app.put("/incidents/{incident_id}",response_model=IncidentResponse)
def update_incident(
    incident_Status : IncidentStatusUpdate,
    incident_id : int,
    db : Session = Depends(get_db)
):
    incident = db.query(Incident).filter(Incident.id == incident_id).first()

    if incident is None:
        raise HTTPException(
                status_code=404,
                detail="Incident not found"
        )
    
    incident.status = incident_Status.status

    db.commit()
    db.refresh(incident)
    return incident
        
        
@app.delete("/incident/{incident_id}")
def delete_incident(
    incident_id : int,
    db : Session = Depends(get_db)
):
    incident = db.query(Incident).filter(
        Incident.id == incident_id
        ).first()

    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    db.delete(incident)
    db.commit()
    

    return {"message": "Incident deleted successfully"}


@app.post("/incidents/{incident_id}/investigations")
def create_investigation(
    investigation: InvestigationCreate,
    incident_id : int,
    db : Session = Depends(get_db)
):

    incident = db.query(Incident).filter(
            Incident.id == incident_id
        ).first()

    if incident is None:
        raise HTTPException(
                    status_code=404,
                    detail="Incident not found"
    )

    
    db_investigation = Investigation(
        incident_id = incident_id,
        confidence = investigation.confidence,
        probable_cause = investigation.probable_cause,
        evidence = investigation.evidence,
        probable_solution = investigation.probable_solution
    )
    db.add(db_investigation)
    db.commit()
    db.refresh(db_investigation)

    

    return db_investigation


@app.get("/incidents/{incident_id}/investigations",response_model=list[InvestigationResponse])
def get_investigations(
    incident_id: int,
    db: Session = Depends(get_db)
):
    investigations = db.query(Investigation).filter(
        Investigation.incident_id==incident_id
        ).all()

    if not investigations :
        raise HTTPException(
            status_code=404,
            detail="Investiagtions not found"
)
    return investigations 