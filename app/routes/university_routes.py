from fastapi import APIRouter, Depends, HTTPException, status

from app.core.dependencies import get_university_service
from app.schemas.university import UniversityCreate, UniversityRead
from app.services.university_service import UniversityService

router = APIRouter(prefix="/universities", tags=["universities"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[UniversityRead])
async def list_universities(service: UniversityService = Depends(get_university_service)):
    return await service.get_all_universities()


@router.get("/{university_id}", status_code=status.HTTP_200_OK, response_model=UniversityRead)
async def get_get_university(university_id: int, service: UniversityService = Depends(get_university_service)):
    university = await service.get_university_by_id(university_id)
    if not university:
        raise HTTPException(status_code=404, detail="University not found")
    return university


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UniversityRead)
async def create_university(request: UniversityCreate, service: UniversityService = Depends(get_university_service)):
    return await service.create_university(request.name)
