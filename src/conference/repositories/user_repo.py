from typing import Optional
from fastapi.encoders import jsonable_encoder
from conference.models.user_model import UserModel
from conference.schemas.user_schema import UserCreate, UserUpdate


class UserRepo:
    @classmethod
    def create_user(cls, user_create: UserCreate) -> UserModel:
        user_jsonable = jsonable_encoder(user_create)
        user_model = UserModel(**user_jsonable)
        with SessionLocal() as db:
            db.add(user_model)
            db.commit()
            db.refresh(user_model)
        return user_model

    @classmethod
    def update_user(cls, user_model: UserModel, user_update: UserUpdate) -> UserModel:
        user_jsonable = jsonable_encoder(user_model)
        update_data = user_update.dict(exclude_unset=True)
        for field in user_jsonable:
            if field in update_data:
                setattr(user_model, field, update_data[field])
        with SessionLocal() as db:
            db.add(user_model)
            db.commit()
            db.refresh(user_model)
        return user_model

    @classmethod
    def get_user_by_username(cls, username: str) -> Optional[UserModel]:
        with SessionLocal() as db:
            domain_user = db.query(UserModel).filter(UserModel.username == username).first()
        return domain_user

    @classmethod
    def check_exists_by_username(cls, username: str) -> bool:
        with SessionLocal() as db:
            exists = db.query(UserModel).filter(
                db.query(UserModel).filter(UserModel.username == username).exists()
            ).scalar()
        return exists
