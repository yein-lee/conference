from conference.models.event_model import EventModel
from conference.schemas.event_schema import EventCreateDTO, EventUpdateDTO, EventOverlapsDTO


class EventRepo:
    @classmethod
    async def create_event(cls, event_create: EventCreateDTO) -> EventModel:
        return await EventModel.objects.create(**event_create.__dict__)

    @classmethod
    async def check_event_overlaps(cls, event_overlaps: EventOverlapsDTO) -> bool:
        overlaps = await EventModel.objects.filter(
            (EventModel.room_id == event_overlaps.room_id) &
            ((EventModel.start_at < event_overlaps.start_at < EventModel.end_at) |
             (EventModel.end_at < event_overlaps.end_at < EventModel.start_at))
        ).exsits()
        return overlaps

    @classmethod
    async def update_event(cls, event_update: EventUpdateDTO) -> EventModel:
        event_model = await EventModel.objects.get(id=event_update.id)
        return await event_model.update(**event_update.dict())
