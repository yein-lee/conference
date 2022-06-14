from typing import Optional
from conference.models.user_model import UserModel
from conference.schemas.user_schema import UserCreate, UserUpdate


class UserRepo:
    @classmethod
    async def create_user(cls, user_create: UserCreate) -> UserModel:
        user_model = await UserModel.objects.create(**user_create.__dict__)
        return user_model

    @classmethod
    async def update_user(cls, user_model: UserModel, user_update: UserUpdate) -> UserModel:
        user_model_dict = user_model.dict()
        update_data = user_update.dict(exclude_unset=True)
        for field in user_model_dict:
            if field in update_data:
                setattr(user_model, field, update_data[field])
        await user_model.update()
        return user_model

    @classmethod
    async def get_user_by_username(cls, username: str) -> UserModel:
        user_model = await UserModel.objects.get(username=username)
        return user_model

    @classmethod
    async def check_exists_by_username(cls, username: str) -> bool:
        exists = await UserModel.objects.filter(username__exact=username).exists()
        return exists
