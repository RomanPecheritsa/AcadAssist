from fastapi import APIRouter, Depends, HTTPException, status

from app.core.dependencies import get_subject_service
from app.schemas.university import SubjectCreate, SubjectRead
from app.services.university import SubjectService

router = APIRouter(prefix="/subjects", tags=["subjects"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[SubjectRead])
async def list_subjects(service: SubjectService = Depends(get_subject_service)):
    return await service.get_all_subjects()


@router.get("/{subject_id}", status_code=status.HTTP_200_OK, response_model=SubjectRead)
async def get_subject(subject_id: int, service: SubjectService = Depends(get_subject_service)):
    subject = await service.get_subject_by_id(subject_id)
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return subject


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SubjectRead)
async def create_subject(request: SubjectCreate, service: SubjectService = Depends(get_subject_service)):
    try:
        return await service.create_subject(request.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{subject_id}", status_code=status.HTTP_200_OK, response_model=SubjectRead)
async def update_subject(
    subject_id: int, request: SubjectCreate, service: SubjectService = Depends(get_subject_service)
):
    subject = await service.get_subject_by_id(subject_id)
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    try:
        return await service.update_subject(subject, request.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{subject_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_subject(subject_id: int, service: SubjectService = Depends(get_subject_service)):
    subject = await service.get_subject_by_id(subject_id)
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    await service.delete_subject(subject)
