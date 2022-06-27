from typing import Optional
from datetime import datetime
from conference.schemas.base_schema import BaseSchema


class EventOverlapsDTO(BaseSchema):
    room_id: int
    start_at: datetime
    end_at: datetime


class EventCreateDTO(BaseSchema):
    room_id: int
    name: str
    create_user_id: int
    start_at: datetime
    end_at: datetime


class EventUpdateDTO(BaseSchema):
    id: int
    room_id: int
    name: Optional[str]
    start_at: Optional[datetime]
    end_at: Optional[datetime]
