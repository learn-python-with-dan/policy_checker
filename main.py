from fastapi import FastAPI
import uvicorn

from src.lifespan import lifespan
from src.routers import *


app = FastAPI(lifespan=lifespan)
app.include_router(comments_router)


if __name__ == '__main__':
    uvicorn.run(app)
