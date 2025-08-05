from fastapi import FastAPI
import uvicorn.config

from app.api.v1.auth import router as auth_router

# Initialize FastAPI
app = FastAPI()

# Include routes
app.include_router(auth_router)

if __name__ == "__main__":
    import uvicorn

    print("Hello world")

    uvicorn.run(app)
