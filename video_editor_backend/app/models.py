from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    size = Column(Float)
    path = Column(String)
    status = Column(String, default="uploaded")
    trimmed_path = Column(String, nullable=True)
    rendered_path = Column(String, nullable=True)
