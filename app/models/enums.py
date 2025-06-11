from enum import Enum


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
