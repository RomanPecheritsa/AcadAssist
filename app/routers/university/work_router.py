from fastapi import APIRouter, Depends, HTTPException, status

from app.core.dependencies import get_work_service
from app.schemas.university import WorkCreate, WorkRead
from app.services.university import WorkService

router = APIRouter(prefix="/works", tags=["works"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[WorkRead])
async def list_works(service: WorkService = Depends(get_work_service)):
    return await service.get_all_works()


@router.get("/{work_id}", status_code=status.HTTP_200_OK, response_model=WorkRead)
async def get_work(work_id: int, service: WorkService = Depends(get_work_service)):
    work = await service.get_work_by_id(work_id)
    if not work:
        raise HTTPException(status_code=404, detail="Work not found")
    return work


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=WorkRead)
async def create_work(request: WorkCreate, service: WorkService = Depends(get_work_service)):
    try:
        return await service.create_work(request.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{work_id}", status_code=status.HTTP_200_OK, response_model=WorkRead)
async def update_work(work_id: int, request: WorkCreate, service: WorkService = Depends(get_work_service)):
    work = await service.get_work_by_id(work_id)
    if not work:
        raise HTTPException(status_code=404, detail="Work not found")

    try:
        return await service.update_work(work, request.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{work_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_work(work_id: int, service: WorkService = Depends(get_work_service)):
    work = await service.get_work_by_id(work_id)
    if not work:
        raise HTTPException(status_code=404, detail="Work not found")
    await service.delete_work(work)
