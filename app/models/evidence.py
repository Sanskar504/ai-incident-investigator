
from app.database.base import Base
from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship




class Evidence(Base):
    __tablename__ = "evidence"

    id : Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    incident_id: Mapped[int] = mapped_column(
        ForeignKey("incidents.id"),
        nullable=False
    )
    
    source : Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    
    content : Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    timestamp : Mapped[datetime] = mapped_column(
        DateTime, 
        nullable=False
    )

    message : Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    severity : Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    
    created_at : Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )


    incident = relationship(
        "Incident",
        back_populates="evidences"
    )