from sqlalchemy.orm import Session

from app.domain.models import User


class UserRepository:
    def create_user(self, user: User, database: Session) -> User:
        database.add(user)
        database.commit()
        database.refresh(user)

        return user
