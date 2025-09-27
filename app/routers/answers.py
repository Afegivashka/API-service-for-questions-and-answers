from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models import Answer, Question
from app.schemas import AnswerCreate, Answer as AnswerSchema

router = APIRouter()

@router.post("/{question_id}/answers/", response_model=AnswerSchema)
async def create_answer(question_id: int, answer: AnswerCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Question).where(Question.id == question_id))
    question = result.scalar_one_or_none()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    db_answer = Answer(question_id=question_id, user_id=answer.user_id, text=answer.text)
    db.add(db_answer)
    await db.commit()
    await db.refresh(db_answer)
    return db_answer

@router.get("/{answer_id}", response_model=AnswerSchema)
async def get_answer(answer_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Answer).where(Answer.id == answer_id))
    answer = result.scalar_one_or_none()
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    return answer

@router.delete("/{answer_id}")
async def delete_answer(answer_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Answer).where(Answer.id == answer_id))
    answer = result.scalar_one_or_none()
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    await db.delete(answer)
    await db.commit()
    return {"message": "Answer deleted"}