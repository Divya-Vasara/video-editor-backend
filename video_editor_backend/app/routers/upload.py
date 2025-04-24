from fastapi import APIRouter, File, UploadFile, Depends
from sqlalchemy.orm import Session
import os, shutil
from app.database import get_db
from app import crud, schemas

router = APIRouter()

@router.post("/upload", response_model=schemas.VideoResponse)
def upload_video(file: UploadFile = File(...), db: Session = Depends(get_db)):
    os.makedirs("videos", exist_ok=True)
    video_path = f"videos/{file.filename}"
    with open(video_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    video = crud.create_video_metadata(db, file.filename, os.path.getsize(video_path), video_path)
    return video
