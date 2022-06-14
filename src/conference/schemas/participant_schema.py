from conference.schemas.base_schema import BaseSchema


class Participant(BaseSchema):
    event_id: int
    user_id: int


class ParticipantCreateRequest(BaseSchema):
    username: str
    event_id: int


class ParticipantCreateResponse(BaseSchema):
    username: str
    name: str
    event_id: int
