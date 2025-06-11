from fastapi import APIRouter, Depends, HTTPException, status

from app.core.dependencies import get_semester_service
from app.schemas.university import SemesterCreate, SemesterRead
from app.services.university import SemesterService

router = APIRouter(prefix="/semesters", tags=["semesters"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[SemesterRead])
async def list_semesters(service: SemesterService = Depends(get_semester_service)):
    return await service.get_all_semesters()


@router.get("/{semester_id}", status_code=status.HTTP_200_OK, response_model=SemesterRead)
async def get_semester(semester_id: int, service: SemesterService = Depends(get_semester_service)):
    semester = await service.get_semester_by_id(semester_id)
    if not semester:
        raise HTTPException(status_code=404, detail="Semester not found")
    return semester


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SemesterRead)
async def create_semester(request: SemesterCreate, service: SemesterService = Depends(get_semester_service)):
    try:
        return await service.create_semester(request.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{semester_id}", status_code=status.HTTP_200_OK, response_model=SemesterRead)
async def update_semester(
    semester_id: int, request: SemesterCreate, service: SemesterService = Depends(get_semester_service)
):
    semester = await service.get_semester_by_id(semester_id)
    if not semester:
        raise HTTPException(status_code=404, detail="Semester not found")

    try:
        return await service.update_semester(semester, request.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{semester_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_semester(semester_id: int, service: SemesterService = Depends(get_semester_service)):
    semester = await service.get_semester_by_id(semester_id)
    if not semester:
        raise HTTPException(status_code=404, detail="Semester not found")
    await service.delete_semester(semester)
