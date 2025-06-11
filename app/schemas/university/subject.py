from pydantic import BaseModel, field_validator


class SubjectBase(BaseModel):
    semester_id: int
    name: str

    @field_validator("semester_id", mode="after")
    def validate_semester_id_positive(cls, value: int) -> int:
        if value < 1:
            raise ValueError("Semester ID must be greater than 0")
        return value


class SubjectCreate(SubjectBase):
    pass


class SubjectRead(SubjectBase):
    id: int

    class Config:
        from_attributes = True
