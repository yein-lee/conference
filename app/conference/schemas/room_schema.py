from conference.schemas.base_schema import BaseSchema


class RoomCreateDTO(BaseSchema):
    workspace_id: int
    name: str
