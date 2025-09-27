from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models import Question
from app.schemas import QuestionCreate, Question as QuestionSchema

router = APIRouter()

@router.get("/", response_model=list[QuestionSchema])
async def get_questions(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Question))
    questions = result.scalars().all()
    return questions

@router.post("/", response_model=QuestionSchema)
async def create_question(question: QuestionCreate, db: AsyncSession = Depends(get_db)):
    db_question = Question(text=question.text)
    db.add(db_question)
    await db.commit()
    await db.refresh(db_question)
    return db_question

@router.get("/{question_id}", response_model=QuestionSchema)
async def get_question(question_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Question).where(Question.id == question_id))
    question = result.scalar_one_or_none()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@router.delete("/{question_id}")
async def delete_question(question_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Question).where(Question.id == question_id))
    question = result.scalar_one_or_none()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    await db.delete(question)
    await db.commit()
    return {"message": "Question and its answers deleted"}