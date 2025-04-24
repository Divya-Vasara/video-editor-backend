from fastapi import FastAPI
from app.routers import upload, trim, subtitles, render, download
from app.database import Base, engine

app = FastAPI(title="Video Editing API")

Base.metadata.create_all(bind=engine)

app.include_router(upload.router, prefix="/api/videos", tags=["Upload"])
app.include_router(trim.router, prefix="/api/videos", tags=["Trim"])
app.include_router(subtitles.router, prefix="/api/videos", tags=["Subtitles"])
app.include_router(render.router, prefix="/api/videos", tags=["Render"])
app.include_router(download.router, prefix="/api/videos", tags=["Download"])
