from conference.schemas.room_schema import RoomCreate
from conference.repositories.room_repo import RoomRepo
from utils.http_exceptions import DuplicationException


class RoomService:
    @classmethod
    def create_room(cls, room_create: RoomCreate):
        exists = RoomRepo().check_room_exists_by_workspace_id_and_name(room_create=room_create)
        if exists:
            raise DuplicationException(detail="name")
        return RoomRepo().create_room(room_create=room_create)
