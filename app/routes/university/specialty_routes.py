from fastapi import APIRouter, Depends, HTTPException, status

from app.core.dependencies import get_specialty_service
from app.schemas.university.specialty import SpecialtyCreate, SpecialtyRead
from app.services.university_service import SpecialtyService

router = APIRouter(prefix="/specialties", tags=["specialties"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[SpecialtyRead])
async def list_specialties(service: SpecialtyService = Depends(get_specialty_service)):
    return await service.get_all_specialties()


@router.get("/{specialty_id}", status_code=status.HTTP_200_OK, response_model=SpecialtyRead)
async def get_specialty(specialty_id: int, service: SpecialtyService = Depends(get_specialty_service)):
    specialty = await service.get_specialty_by_id(specialty_id)
    if not specialty:
        raise HTTPException(status_code=404, detail="Specialty not found")
    return specialty


@router.post("/specialties", status_code=status.HTTP_201_CREATED, response_model=SpecialtyRead)
async def create_specialty(
    request: SpecialtyCreate,
    service: SpecialtyService = Depends(get_specialty_service),  # <-- Явно указываем
):
    return await service.create_specialty(request.dict())


@router.put("/specialties/{specialty_id}", status_code=status.HTTP_200_OK, response_model=SpecialtyRead)
async def update_specialty(
    specialty_id: int,
    request: SpecialtyCreate,
    service: SpecialtyService = Depends(get_specialty_service),  # <-- Явно указываем
):
    specialty = await service.get_specialty_by_id(specialty_id)
    if not specialty:
        raise HTTPException(status_code=404, detail="Specialty not found")
    return await service.update_specialty(specialty, request.dict())


@router.delete("/specialties/{specialty_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_specialty(
    specialty_id: int,
    service: SpecialtyService = Depends(get_specialty_service),  # <-- Явно указываем
):
    specialty = await service.get_specialty_by_id(specialty_id)
    if not specialty:
        raise HTTPException(status_code=404, detail="Specialty not found")
    await service.delete_specialty(specialty)
