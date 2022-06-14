from conference.models.event_model import EventModel
from conference.models.participant_model import ParticipantModel
from conference.schemas.event_schema import EventCreate, CheckEventOverlaps
from conference.schemas.participant_schema import Participant


class EventRepo:
    @classmethod
    def check_event_time_overlaps(cls, check_event_overlaps: CheckEventOverlaps):
        with SessionLocal() as db:
            overlaps = db.query(EventModel).\
                filter(
                    db.query(EventModel).filter(
                        EventModel.room_id == check_event_overlaps.room_id,
                        EventModel.start_at < check_event_overlaps.start_at < EventModel.end_at |
                        EventModel.end_at < check_event_overlaps.end_at < EventModel.start_at).exists()
            ).scalar()
        return overlaps

    @classmethod
    def create_event(cls, event_create: EventCreate) -> EventModel:
        event_model = EventModel(**event_create.dict())
        with SessionLocal() as db:
            db.add(event_model)
            db.commit()
            db.refresh(event_model)
        return event_model

    @classmethod
    def check_event_exists_by_id(cls, event_id: int) -> bool:
        with SessionLocal() as db:
            exists = db.query(EventModel).filter(
                db.query(EventModel).filter(EventModel.id == event_id).exists()
            ).scalar()
        return exists

    @classmethod
    def get_event_by_id(cls, event_id: int) -> EventModel:
        with SessionLocal() as db:
            event_model = db.query(EventModel).filter(EventModel.id == event_id).first()
        return event_model

    @classmethod
    def create_participant(cls, participant_create: Participant) -> ParticipantModel:
        participant_model = ParticipantModel(**participant_create.dict())
        with SessionLocal() as db:
            db.add(participant_model)
            db.commit()
            db.refresh(participant_model)
        return participant_model
