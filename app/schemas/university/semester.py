from datetime import date

from pydantic import BaseModel, field_validator


class SemesterBase(BaseModel):
    specialty_id: int
    number: int
    cost: int
    deadline: date

    @field_validator("number")
    def check_number_must_be_positive(cls, v):
        if v < 1:
            raise ValueError("Semester number must be greater than 0")
        return v


class SemesterCreate(SemesterBase):
    pass


class SemesterRead(SemesterBase):
    id: int

    class Config:
        from_attributes = True
