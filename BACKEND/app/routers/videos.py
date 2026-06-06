from fastapi import APIRouter, HTTPException
from sqlmodel import select
from sqlalchemy.sql.expression import func
from db import SessionDep
from models import Videos, VideosCreate, Comments, CommentsCreate

router = APIRouter()

@router.get("/videos")
def get_videos(session: SessionDep):
    return session.exec(select(Videos)).all()

@router.post("/videos")
def create_video(video_data: VideosCreate, session: SessionDep):
    video = Videos.model_validate(video_data.model_dump())
    session.add(video)
    session.commit()
    session.refresh(video)
    return video

@router.get("/videos/recomendaciones/{categoria}")
def get_recomendaciones(categoria: str, session: SessionDep):
    query = select(Videos).where(Videos.categoria == categoria).order_by(func.random()).limit(10)
    return session.exec(query).all()

@router.get("/videos/{video_id}")
def get_video_by_id(video_id: int, session: SessionDep):
    video_db = session.get(Videos, video_id)
    if not video_db:
        raise HTTPException(status_code=404, detail="Video not found")
    return video_db

@router.get("/videos/{video_id}/comments")
def get_comments_by_video(video_id: int, session: SessionDep):
    statement = select(Comments).where(Comments.video_id == video_id)
    return session.exec(statement).all()

@router.post("/comments")
def create_comment(comment_data: CommentsCreate, session: SessionDep):
    db_comment = Comments.model_validate(comment_data)
    session.add(db_comment)
    session.commit()
    session.refresh(db_comment)
    return db_comment