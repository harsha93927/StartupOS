from sqlalchemy import Column, Integer, String, Text, JSON
from app.db.session import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    workspace_folder = Column(String)
    vision = Column(Text)
    status = Column(String, default="created")
    plan_type = Column(String, default="free")
    meta_data = Column(JSON, nullable=True)
