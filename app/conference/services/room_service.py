from conference.schemas.room_schema import RoomCreate
from conference.repositories.room_repo import RoomRepo


class RoomService:
    @classmethod
    async def create_room(cls, room_in: RoomCreate):
        return await RoomRepo().create_room(room_in=room_in)
