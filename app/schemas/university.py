from pydantic import BaseModel


class UniversityRead(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
