from datetime import date
from enum import Enum

from sqlalchemy import ForeignKey, String
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


class University(Base):
    __tablename__ = "universities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    specialties: Mapped[list["Specialty"]] = relationship(back_populates="university")


class Specialty(Base):
    __tablename__ = "specialties"

    id: Mapped[int] = mapped_column(primary_key=True)
    university_id: Mapped[int] = mapped_column(ForeignKey("universities.id"))
    name: Mapped[str] = mapped_column(String(100))
    total_cost: Mapped[int]
    deadline: Mapped[date]
    semesters_count: Mapped[int]
    education_form_type: Mapped[EducationFormType]

    university: Mapped["University"] = relationship(back_populates="specialties")
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


class Work(Base):
    __tablename__ = "works"

    id: Mapped[int] = mapped_column(primary_key=True)
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    title: Mapped[str] = mapped_column(String(200))
    cost: Mapped[int]
    deadline: Mapped[date]
    work_type: Mapped[WorkType]

    subject: Mapped["Subject"] = relationship(back_populates="works")
