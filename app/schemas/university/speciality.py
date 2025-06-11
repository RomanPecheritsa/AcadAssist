from datetime import date

from pydantic import BaseModel, field_validator

from app.models.enums import EducationFormType


class SpecialityBase(BaseModel):
    name: str
    cost: int
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

    @field_validator("university_id", mode="after")
    def validate_university_id_positive(cls, value: int) -> int:
        if value < 1:
            raise ValueError("University ID must be greater than 0")
        return value

    @field_validator("cost", mode="after")
    def validate_cost_positive(cls, value) -> int:
        if value < 0:
            raise ValueError("Cost should not be negative")
        return value

    @field_validator("semesters_count", mode="after")
    def validate_semesters_count_positive(cls, value) -> int:
        if value < 1:
            raise ValueError("Semester count must be greater than 0")
        return value


class SpecialityCreate(SpecialityBase):
    pass


class SpecialityRead(SpecialityBase):
    id: int

    class Config:
        from_attributes = True
