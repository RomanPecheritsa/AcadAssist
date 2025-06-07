from fastapi import APIRouter, Depends
from starlette import status

from app.backend.dependencies import get_university_service
from app.schemas.university import UniversityRead
from app.services.university_service import UniversityService

router = APIRouter(prefix="/universities", tags=["universities"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[UniversityRead])
async def list_universities(service: UniversityService = Depends(get_university_service)):
    return await service.get_all_universities()
