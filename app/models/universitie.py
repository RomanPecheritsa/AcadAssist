from datetime import date
from enum import Enum

from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class EducationFormType(str, Enum):
    FULL_TIME = "очная"
    PART_TIME = "заочная"


class WorkType(str, Enum):
    ESSAY = "эссе"
    TEST = "контрольная"
    REPORT = "реферат"
    COURSEWORK = "курсовая"
    COURSE_PROJECT = "курсовой проект"
    THESIS = "ВКР"


university_education_forms = Table(
    "university_education_forms",
    Base.metadata,
    Column("university_id", ForeignKey("universities.id"), primary_key=True),
    Column("education_form_id", ForeignKey("education_forms.id"), primary_key=True),
)


class University(Base):
    __tablename__ = "universities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    specialties: Mapped[list["Specialty"]] = relationship(back_populates="university")


class EducationForm(Base):
    __tablename__ = "education_forms"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[EducationFormType] = mapped_column()

    specialties: Mapped[list["Specialty"]] = relationship(back_populates="education_form")


class Specialty(Base):
    __tablename__ = "specialties"

    id: Mapped[int] = mapped_column(primary_key=True)
    university_id: Mapped[int] = mapped_column(ForeignKey("universities.id"))
    education_form_id: Mapped[int] = mapped_column(ForeignKey("education_forms.id"))
    name: Mapped[str] = mapped_column(String(100))
    total_cost: Mapped[int]
    deadline: Mapped[date]
    semesters_count: Mapped[int]

    university: Mapped["University"] = relationship(back_populates="specialties")
    education_form: Mapped["EducationForm"] = relationship(back_populates="specialties")
    semesters: Mapped[list["Semester"]] = relationship(back_populates="specialty")


class Semester(Base):
    __tablename__ = "semesters"

    id: Mapped[int] = mapped_column(primary_key=True)
    specialty_id: Mapped[int] = mapped_column(ForeignKey("specialties.id"))
    number: Mapped[int]
    cost: Mapped[int]
    deadline: Mapped[date]

    specialty: Mapped["Specialty"] = relationship(back_populates="semesters")
    subjects: Mapped[list["Subject"]] = relationship(back_populates="semester")


class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(primary_key=True)
    semester_id: Mapped[int] = mapped_column(ForeignKey("semesters.id"))
    name: Mapped[str] = mapped_column(String(100))

    semester: Mapped["Semester"] = relationship(back_populates="subjects")
    works: Mapped[list["Work"]] = relationship(back_populates="subject")


class WorkTypeModel(Base):
    __tablename__ = "work_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[WorkType] = mapped_column()

    works: Mapped[list["Work"]] = relationship(back_populates="work_type")


class Work(Base):
    __tablename__ = "works"

    id: Mapped[int] = mapped_column(primary_key=True)
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    work_type_id: Mapped[int] = mapped_column(ForeignKey("work_types.id"))
    title: Mapped[str] = mapped_column(String(200))
    cost: Mapped[int]
    deadline: Mapped[date]

    subject: Mapped["Subject"] = relationship(back_populates="works")
    work_type: Mapped["WorkTypeModel"] = relationship(back_populates="works")
