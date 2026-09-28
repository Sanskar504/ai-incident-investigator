from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship 
from sqlalchemy import Integer,String,ForeignKey




class Investigation(Base):
    __tablename__ = "investigations"

    incident = relationship(
        "Incident",
        back_populates="investigations",
        
        )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    incident_id: Mapped[int] = mapped_column(
    ForeignKey("incidents.id"),
    nullable=False
)
    probable_cause : Mapped[str] = mapped_column(String(255),nullable=False)
    confidence: Mapped[float] = mapped_column(nullable=False)
    evidence : Mapped[str] = mapped_column(String(255),nullable=False)
    probable_solution : Mapped[str] = mapped_column(String(255),nullable=False)
