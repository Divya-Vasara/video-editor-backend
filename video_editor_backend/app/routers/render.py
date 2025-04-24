from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, ffmpeg_utils, schemas

router = APIRouter()

@router.post("/{video_id}/render", response_model=schemas.VideoResponse)
def render_final_video(video_id: int, db: Session = Depends(get_db)):
    video = crud.get_video_by_id(db, video_id)
    if not video or not video.trimmed_path:
        raise HTTPException(status_code=404, detail="Nothing to render")

    final_path = f"videos/rendered_{video.filename}"
    ffmpeg_utils.merge_video_parts(video.path, video.trimmed_path, video.trimmed_path, final_path)
    crud.update_video_rendered_path(db, video_id, final_path)
    return crud.get_video_by_id(db, video_id)
