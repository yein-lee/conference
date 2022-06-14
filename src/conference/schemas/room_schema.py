from conference.schemas.base_schema import BaseSchema


class Room(BaseSchema):
    workspace_id: int
    name: str


class RoomCreate(Room):
    ...
