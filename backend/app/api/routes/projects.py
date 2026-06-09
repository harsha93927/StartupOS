from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.project import Project
from app.services.subscription_service import SubscriptionService
from app.memory.project_memory import ProjectMemory

router = APIRouter()

class ProjectCreate(BaseModel):
    name: str
    workspace_folder: str
    vision: str

class PremiumUnlock(BaseModel):
    password: str

@router.post("/")
async def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    if not SubscriptionService.can_create_project(db, "demo_user"):
        raise HTTPException(status_code=403, detail="Project limit reached for free plan. Unlock premium.")

    db_project = Project(
        name=project.name,
        workspace_folder=project.workspace_folder,
        vision=project.vision
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)

    memory = ProjectMemory(project.workspace_folder)
    intent = {
        "id": db_project.id,
        "name": db_project.name,
        "vision": db_project.vision,
        "plan_type": db_project.plan_type
    }
    memory.save_json("startup_intent.json", intent)
    return {"message": "Project created successfully", "project": intent}

@router.post("/{project_id}/unlock")
async def unlock_project(project_id: int, unlock: PremiumUnlock, db: Session = Depends(get_db)):
    if not SubscriptionService.unlock_premium(unlock.password):
        raise HTTPException(status_code=401, detail="Invalid premium password")

    db_project = db.query(Project).filter(Project.id == project_id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")

    db_project.plan_type = "premium"
    db.commit()
    return {"message": "Project upgraded to Premium"}
