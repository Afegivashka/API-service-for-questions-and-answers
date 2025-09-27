from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers.questions import router as questions_router
from app.routers.answers import router as answers_router
from app.database import engine, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan ,title="QA API Service")

app.include_router(questions_router, prefix="/questions", tags=["questions"])
app.include_router(answers_router, prefix="/answers", tags=["answers"])