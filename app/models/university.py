from datetime import date

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base
from app.models.enums import EducationFormType, WorkType


class University(Base):
    __tablename__ = "universities"

    name: Mapped[str] = mapped_column(String(100), unique=True)

    specialties: Mapped[list["Speciality"]] = relationship(back_populates="university", cascade="all, delete-orphan")


class Speciality(Base):
    __tablename__ = "specialties"

    university_id: Mapped[int] = mapped_column(ForeignKey("universities.id", ondelete="CASCADE"))
    name: Mapped[str] = mapped_column(String(100))
    cost: Mapped[int]
    deadline: Mapped[date]
    semesters_count: Mapped[int]
    education_form_type: Mapped[EducationFormType]

    university: Mapped["University"] = relationship(back_populates="specialties")
    semesters: Mapped[list["Semester"]] = relationship(back_populates="speciality", cascade="all, delete-orphan")


class Semester(Base):
    __tablename__ = "semesters"

    speciality_id: Mapped[int] = mapped_column(ForeignKey("specialties.id", ondelete="CASCADE"))
    number: Mapped[int]
    cost: Mapped[int]
    deadline: Mapped[date]

    speciality: Mapped["Speciality"] = relationship(back_populates="semesters")
    subjects: Mapped[list["Subject"]] = relationship(back_populates="semester", cascade="all, delete-orphan")


class Subject(Base):
    __tablename__ = "subjects"

    semester_id: Mapped[int] = mapped_column(ForeignKey("semesters.id", ondelete="CASCADE"))
    name: Mapped[str] = mapped_column(String(100))

    semester: Mapped["Semester"] = relationship(back_populates="subjects")
    works: Mapped[list["Work"]] = relationship(back_populates="subject", cascade="all, delete-orphan")


class Work(Base):
    __tablename__ = "works"

    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id", ondelete="CASCADE"))
    title: Mapped[str] = mapped_column(String(200))
    cost: Mapped[int]
    deadline: Mapped[date]
    work_type: Mapped[WorkType]

    subject: Mapped["Subject"] = relationship(back_populates="works")
