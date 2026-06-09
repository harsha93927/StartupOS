from app.models.project import Project
from sqlalchemy.orm import Session

class SubscriptionService:
    @staticmethod
    def can_create_project(db: Session, user_id: str) -> bool:
        # In a real app we'd filter by user_id
        count = db.query(Project).count()
        # For demo, let's assume the first project is free
        if count >= 1:
            # Check if any project is premium
            premium_exists = db.query(Project).filter(Project.plan_type == "premium").first()
            if not premium_exists:
                return False
            # Premium allows up to 10
            return count < 10
        return True

    @staticmethod
    def get_agent_limit(project: Project) -> int:
        if project.plan_type == "premium":
            return 10
        return 4

    @staticmethod
    def unlock_premium(password: str) -> bool:
        return password == "123456"
