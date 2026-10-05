from sqlalchemy.orm import Session

from app.models.evidence import Evidence
from app.services.evidence_collector import collect_log_evidence


def save_log_evidence(
    db: Session,
    incident_id: int,
    log_file_path: str
):
    evidence_data = collect_log_evidence(
        incident_id=incident_id,
        log_file_path=log_file_path
    )

    db_evidence = Evidence(
        incident_id=evidence_data["incident_id"],
        source=evidence_data["source"],
        content=evidence_data["content"]
    )

    db.add(db_evidence)
    db.commit()
    db.refresh(db_evidence)

    return db_evidence