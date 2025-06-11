from datetime import date

from pydantic import BaseModel, field_validator

from app.models.enums import WorkType


class WorkBase(BaseModel):
    subject_id: int
    title: str
    cost: int
    deadline: date
    work_type: WorkType

    @field_validator("subject_id", mode="after")
    def validate_subject_id_positive(cls, value: int) -> int:
        if value < 1:
            raise ValueError("Subject ID must be greater than 0")
        return value

    @field_validator("cost", mode="after")
    def validate_cost_positive(cls, value) -> int:
        if value < 0:
            raise ValueError("Cost should not be negative")
        return value

    @field_validator("deadline", mode="before")
    def parse_deadline(cls, value):
        if isinstance(value, str):
            try:
                return date.fromisoformat(value)
            except ValueError:
                raise ValueError("Invalid date format. Expected ISO format: YYYY-MM-DD")
        return value


class WorkCreate(WorkBase):
    pass


class WorkRead(WorkBase):
    id: int

    class Config:
        from_attributes = True
