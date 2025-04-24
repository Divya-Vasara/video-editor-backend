from sqlalchemy.orm import Session
from app import models

def create_video_metadata(db: Session, filename: str, size: float, path: str):
    video = models.Video(filename=filename, size=size, path=path)
    db.add(video)
    db.commit()
    db.refresh(video)
    return video

def update_video_trim_path(db: Session, video_id: int, trimmed_path: str):
    video = db.query(models.Video).get(video_id)
    video.trimmed_path = trimmed_path
    db.commit()
    return video

def update_video_rendered_path(db: Session, video_id: int, rendered_path: str):
    video = db.query(models.Video).get(video_id)
    video.rendered_path = rendered_path
    video.status = "rendered"
    db.commit()
    return video

def get_video_by_id(db: Session, video_id: int):
    return db.query(models.Video).get(video_id)
