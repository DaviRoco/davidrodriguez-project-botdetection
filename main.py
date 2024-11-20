from fastapi import FastAPI

from adapters.input.rest.ip_usage_api import ip_usage_router
from adapters.input.rest.url_ratio_api import url_ratio_router
from adapters.input.rest.actuator_api import actuator_router

app = FastAPI()
routers = [
    ip_usage_router,
    url_ratio_router,
]

app.include_router(actuator_router)
for router in routers:
    app.include_router(router, prefix="/api/v1")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
