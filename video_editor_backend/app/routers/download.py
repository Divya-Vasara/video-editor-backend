from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud

router = APIRouter()

@router.get("/{video_id}/download")
def download_video(video_id: int, db: Session = Depends(get_db)):
    video = crud.get_video_by_id(db, video_id)
    if not video or not video.rendered_path:
        raise HTTPException(status_code=404, detail="Rendered video not found")
    return FileResponse(video.rendered_path, media_type='application/octet-stream', filename=f"final_{video.filename}")
