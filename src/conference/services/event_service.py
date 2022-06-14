from conference.services.user_service import UserService
from conference.models.event_model import Event as EventModel
from conference.models.participant_model import Participant as ParticipantModel
from conference.schemas.event_schema import EventCreate, CheckEventOverlaps
from conference.schemas.team_schema import TeamExist
from conference.schemas.participant_schema import Participant, ParticipantCreateRequest
from conference.repositories.event_repo import EventRepo
from conference.services.team_service import TeamService
from utils.http_exceptions import DuplicationException, NotFoundException


class EventService:
    @classmethod
    def create_event(cls, event_create: EventCreate) -> EventModel:
        check_event_overlaps = CheckEventOverlaps(**event_create.__dict__)
        overlaps = EventRepo().check_event_time_overlaps(check_event_overlaps=check_event_overlaps)
        if overlaps:
            raise DuplicationException(detail="time")
        event_create = EventCreate(**event_create.__dict__)
        return EventRepo().create_event(event_create=event_create)

    @classmethod
    def add_participant(cls, participant_create_request: ParticipantCreateRequest) -> ParticipantModel:
        user_model = UserService().get_user_by_username(username=participant_create_request.username)
        event_model = cls.get_event_by_id(event_id=participant_create_request.event_id)
        team_exist = TeamExist(**user_model.__dict__, **event_model.__dict__)
        TeamService().check_team_exists(team_exist=team_exist)
        participant_create = Participant(user_id=user_model.id, event_id=event_model.id)
        return EventRepo().create_participant(participant_create=participant_create)

    @classmethod
    def get_event_by_id(cls, event_id: int) -> EventModel:
        exists = EventRepo().check_event_exists_by_id(event_id=event_id)
        if not exists:
            raise NotFoundException(detail="team")
        return EventRepo().get_event_by_id(event_id=event_id)
