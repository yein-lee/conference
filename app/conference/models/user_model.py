from ormar import Model, Integer, String
from conference.models.base_model import BaseMeta


class UserModel(Model):
    class Meta(BaseMeta):
        tablename = "users"

    id: int = Integer(primary_key=True, index=True)
    username: str = String(max_length=16, unique=True, index=True, nullable=False)
    name: str = String(max_length=16, unique=True)
    password: str = String(max_length=60)
