from datetime import date
from enum import Enum

from pydantic import BaseModel, field_validator


class EducationFormType(str, Enum):
    FULL_TIME = "очная"
    PART_TIME = "заочная"


class SpecialtyBase(BaseModel):
    name: str
    total_cost: int
    deadline: date
    semesters_count: int
    education_form_type: EducationFormType
    university_id: int

    @field_validator("deadline", mode="before")
    def parse_deadline(cls, value):
        if isinstance(value, str):
            try:
                return date.fromisoformat(value)
            except ValueError:
                raise ValueError("Invalid date format. Expected ISO format: YYYY-MM-DD")
        return value


class SpecialtyCreate(SpecialtyBase):
    pass


class SpecialtyRead(SpecialtyBase):
    id: int

    class Config:
        from_attributes = True
