from datetime import date

from pydantic import BaseModel, field_validator


class SemesterBase(BaseModel):
    speciality_id: int
    number: int
    cost: int
    deadline: date

    @field_validator("deadline", mode="before")
    def parse_deadline(cls, value):
        if isinstance(value, str):
            try:
                return date.fromisoformat(value)
            except ValueError:
                raise ValueError("Invalid date format. Expected ISO format: YYYY-MM-DD")
        return value

    @field_validator("number")
    def check_number_must_be_positive(cls, v):
        if v < 1:
            raise ValueError("Semester number must be greater than 0")
        return v

    @field_validator("cost", mode="after")
    def validate_cost_positive(cls, value) -> int:
        if value < 0:
            raise ValueError("Cost should not be negative")
        return value


class SemesterCreate(SemesterBase):
    pass


class SemesterRead(SemesterBase):
    id: int

    class Config:
        from_attributes = True
