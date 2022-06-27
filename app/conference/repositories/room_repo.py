from conference.models.room_model import RoomModel
from conference.schemas.room_schema import RoomCreateDTO


class RoomRepo:
    @classmethod
    async def create_room(cls, room_in: RoomCreateDTO) -> RoomModel:
        return await RoomModel.objects.create(**room_in.__dict__)
