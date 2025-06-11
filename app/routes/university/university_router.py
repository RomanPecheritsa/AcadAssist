from fastapi import APIRouter, Depends, HTTPException, status

from app.core.dependencies import get_university_service
from app.schemas.university.university import UniversityCreate, UniversityRead
from app.services.university_service import UniversityService

router = APIRouter(prefix="/universities", tags=["universities"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[UniversityRead])
async def list_universities(service: UniversityService = Depends(get_university_service)):
    return await service.get_all_universities()


@router.get("/{university_id}", status_code=status.HTTP_200_OK, response_model=UniversityRead)
async def get_university(university_id: int, service: UniversityService = Depends(get_university_service)):
    university = await service.get_university_by_id(university_id)
    if not university:
        raise HTTPException(status_code=404, detail="University not found")
    return university


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UniversityRead)
async def create_university(request: UniversityCreate, service: UniversityService = Depends(get_university_service)):
    return await service.create_university(name=request.name)


@router.put("/{university_id}", status_code=status.HTTP_200_OK, response_model=UniversityRead)
async def update_university(
    university_id: int, request: UniversityCreate, service: UniversityService = Depends(get_university_service)
):
    university = await service.get_university_by_id(university_id)
    if not university:
        raise HTTPException(status_code=404, detail="University not found")
    return await service.update_university(university, name=request.name)


@router.delete("/{university_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_university(university_id: int, service: UniversityService = Depends(get_university_service)):
    university = await service.get_university_by_id(university_id)
    if not university:
        raise HTTPException(status_code=404, detail="University not found")
    await service.delete_university(university)
