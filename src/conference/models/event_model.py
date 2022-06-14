from datetime import datetime
from ormar import Model, Integer, String, ForeignKey, Text, DateTime
from base_model import BaseMeta
from room_model import RoomModel
from user_model import UserModel


class EventModel(Model):
    class Meta(BaseMeta):
        tablename = "events"

    id: int = Integer(primary_key=True, index=True)
    room_id: int = ForeignKey(RoomModel)
    name: str = String(max_length=100)
    description: str = Text()
    create_user_id: int = ForeignKey(UserModel)
    start_at: datetime = DateTime()
    end_at: datetime = DateTime()
