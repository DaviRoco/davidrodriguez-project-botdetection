from fastapi import APIRouter

actuator_router = APIRouter()


@actuator_router.get("/actuator/health")
async def health_check():
    return {"status": "up"}
