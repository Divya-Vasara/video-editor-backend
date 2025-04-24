from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, ffmpeg_utils, schemas

router = APIRouter()

@router.post("/{video_id}/trim", response_model=schemas.VideoResponse)
def trim_video(video_id: int, start: float, end: float, db: Session = Depends(get_db)):
    video = crud.get_video_by_id(db, video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    trimmed_path = f"videos/trimmed_{video.filename}"
    ffmpeg_utils.trim_video(video.path, trimmed_path, start, end)
    crud.update_video_trim_path(db, video_id, trimmed_path)
    return crud.get_video_by_id(db, video_id)
