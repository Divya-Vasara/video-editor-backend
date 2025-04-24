from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, ffmpeg_utils, schemas

router = APIRouter()

@router.post("/{video_id}/subtitles", response_model=schemas.VideoResponse)
def add_subtitles(video_id: int, text: str, start: float, end: float, db: Session = Depends(get_db)):
    video = crud.get_video_by_id(db, video_id)
    if not video or not video.trimmed_path:
        raise HTTPException(status_code=404, detail="Trimmed video not found")

    subtitle_path = f"videos/subtitled_{video.filename}"
    ffmpeg_utils.overlay_subtitles(video.trimmed_path, subtitle_path, text, start, end)
    crud.update_video_trim_path(db, video_id, subtitle_path)  # update to latest
    return crud.get_video_by_id(db, video_id)
