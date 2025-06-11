from .semester_router import router as semester_router
from .speciality_router import router as speciality_router
from .subject_router import router as subject_router
from .university_router import router as university_router
from .work_router import router as work_router

__all__ = ["semester_router", "speciality_router", "subject_router", "university_router", "work_router"]
