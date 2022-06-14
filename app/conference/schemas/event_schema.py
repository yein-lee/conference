from datetime import datetime
from conference.schemas.base_schema import BaseSchema


class Event(BaseSchema):
    id: int
    room_id: int
    name: str
    create_user_id: int
    start_at: datetime
    end_at: datetime


class CheckEventOverlaps(BaseSchema):
    room_id: int
    start_at: datetime
    end_at: datetime


class EventCreateRequest(BaseSchema):
    room_id: int
    name: str
    start_at: datetime
    end_at: datetime


class EventCreate(BaseSchema):
    room_id: int
    name: str
    create_user_id: int
    start_at: datetime
    end_at: datetime
