import fastapi
import routers
import uvicorn

app = fastapi.FastAPI(title="Demo Fake vs Real Async")
app.include_router(routers.router, prefix="/api/v1")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
