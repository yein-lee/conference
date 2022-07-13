from datetime import datetime
from ormar import Model, Integer, String, ForeignKey, Text, DateTime
from conference.models.base_model import BaseMeta, BaseConfig
from conference.models.room_model import RoomModel
from conference.models.user_model import UserModel


class EventModel(Model):
    class Meta(BaseMeta):
        tablename = "events"

    class Config(BaseConfig):
        ...

    id: int = Integer(primary_key=True, index=True)
    room_id: int = ForeignKey(RoomModel)
    name: str = String(max_length=100)
    description: str = Text()
    create_user_id: int = ForeignKey(UserModel)
    start_at: datetime = DateTime()
    end_at: datetime = DateTime()
