from sqlmodel import Field, SQLModel, Relationship

class Comments(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    texto: str
    video_id: int = Field(foreign_key="videos.id")
    video: "Videos" = Relationship(back_populates="comments")

class Videos(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titulo: str 
    source: str
    categoria: str
    estado: bool = True
    poster: str = "" 
    comments: list["Comments"] = Relationship(back_populates="video")

class CommentsCreate(SQLModel):
    texto: str
    video_id: int

class VideosCreate(SQLModel):
    titulo: str
    source: str
    categoria: str
    poster: str = "" 