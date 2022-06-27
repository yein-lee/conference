from conference.schemas.event_schema import EventCreateDTO, EventUpdateDTO, EventOverlapsDTO
from conference.repositories.event_repo import EventRepo
from conference.models.event_model import EventModel
from utils.http_exceptions import DuplicationException


class EventService:
    @classmethod
    async def create_event(cls, event_create: EventCreateDTO) -> EventModel:
        event_overlaps = EventOverlapsDTO(**event_create.dict())
        await cls.check_event_overlaps(event_overlaps=event_overlaps)
        return await EventRepo.create_event(event_create=event_create)

    @classmethod
    async def check_event_overlaps(cls, event_overlaps: EventOverlapsDTO) -> bool:
        overlaps = await EventRepo.check_event_overlaps(event_overlaps=event_overlaps)
        if overlaps:
            raise DuplicationException(detail="event")
        return True

    @classmethod
    async def update_event(cls, event_update: EventUpdateDTO) -> EventModel:
        event_overlaps = EventOverlapsDTO(**event_update.dict())
        await cls.check_event_overlaps(event_overlaps=event_overlaps)
        return await EventRepo.update_event(event_update)
