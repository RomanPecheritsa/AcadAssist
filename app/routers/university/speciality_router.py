from fastapi import APIRouter, Depends, HTTPException, status

from app.core.dependencies import get_speciality_service
from app.schemas.university import SpecialityCreate, SpecialityRead
from app.services.university import SpecialityService

router = APIRouter(prefix="/specialties", tags=["specialties"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[SpecialityRead])
async def list_specialties(service: SpecialityService = Depends(get_speciality_service)):
    return await service.get_all_specialties()


@router.get("/{speciality_id}", status_code=status.HTTP_200_OK, response_model=SpecialityRead)
async def get_speciality(speciality_id: int, service: SpecialityService = Depends(get_speciality_service)):
    speciality = await service.get_speciality_by_id(speciality_id)
    if not speciality:
        raise HTTPException(status_code=404, detail="Speciality not found")
    return speciality


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SpecialityRead)
async def create_speciality(
    request: SpecialityCreate,
    service: SpecialityService = Depends(get_speciality_service),
):
    try:
        return await service.create_speciality(request.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{speciality_id}", status_code=status.HTTP_200_OK, response_model=SpecialityRead)
async def update_speciality(
    speciality_id: int, request: SpecialityCreate, service: SpecialityService = Depends(get_speciality_service)
):
    speciality = await service.get_speciality_by_id(speciality_id)
    if not speciality:
        raise HTTPException(status_code=404, detail="Speciality not found")

    try:
        updated_speciality = await service.update_speciality(speciality, request.model_dump())
        return updated_speciality
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{speciality_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_speciality(
    speciality_id: int,
    service: SpecialityService = Depends(get_speciality_service),
):
    speciality = await service.get_speciality_by_id(speciality_id)
    if not speciality:
        raise HTTPException(status_code=404, detail="Speciality not found")
    await service.delete_speciality(speciality)
