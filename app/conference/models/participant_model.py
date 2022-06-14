from ormar import Model, Integer, ForeignKey
from conference.models.base_model import BaseMeta
from conference.models.event_model import EventModel
from conference.models.user_model import UserModel


class ParticipantModel(Model):
    class Meta(BaseMeta):
        tablename = "participants"

    id: int = Integer(primary_key=True, index=True)
    event_id: int = ForeignKey(EventModel)
    user_id: int = ForeignKey(UserModel)
