from fastapi import APIRouter

import services


router = APIRouter()


@router.get("/health-check")
async def health_check() -> dict:
    """
    Health check endpoint
    """
    return {"status": "ok"}


@router.get("/fake-async")
async def do() -> int:
    """
    This function is marked async, but it calls a synchronous function.
    It will block the event loop.
    """
    return services.heavy_computation_work()


@router.get("/real-async")
async def do() -> int:
    """
    This function is marked async and calls an async function.
    It will not block the event loop
    """
    return await services.heavy_computation_work_async()
