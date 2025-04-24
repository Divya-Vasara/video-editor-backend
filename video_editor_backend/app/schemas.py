from pydantic import BaseModel

class VideoResponse(BaseModel):
    id: int
    filename: str
    status: str

    class Config:
        orm_mode = True
