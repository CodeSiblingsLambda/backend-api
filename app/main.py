from fastapi import FastAPI
import uvicorn.config

# Initialize FastAPI
app = FastAPI()

if __name__ == "__main__":
    import uvicorn
    print("Hello world")

    uvicorn.run(app)