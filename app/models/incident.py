from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime, Enum as SQLEnum, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.database.base import Base



class Base(DeclarativeBase):
    pass


class IncidentStatus(str, Enum):
    OPEN = "OPEN"
    INVESTIGATING = "INVESTIGATING"
    ACTION_REQUIRED = "ACTION_REQUIRED"
    RESOLVED = "RESOLVED"


class Incident(Base):
    __tablename__ = "incidents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    repository: Mapped[str] = mapped_column(String(255), nullable=False)

    commit_id: Mapped[str] = mapped_column(String(255), nullable=False)

    build_id: Mapped[int] = mapped_column(Integer, nullable=False)

    status: Mapped[IncidentStatus] = mapped_column(
        SQLEnum(IncidentStatus),
        nullable=False,
        default=IncidentStatus.OPEN,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )