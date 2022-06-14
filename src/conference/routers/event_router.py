from fastapi import APIRouter, Depends, Body
from conference.routers.auth_dep import get_username_of_current_user
from conference.services.event_service import EventService
from conference.schemas.event_schema import Event, EventCreate, EventCreateRequest
from conference.schemas.participant_schema import Participant, ParticipantCreateRequest, ParticipantCreateResponse

router = APIRouter(dependencies=[Depends(get_username_of_current_user)])


@router.post("/", response_model=Event)
def create_event(
        username: str = Depends(get_username_of_current_user),
        event_in: EventCreateRequest = Body(...)
) -> Event:
    event_create = EventCreate(**event_in.__dict__, username=username)
    return EventService().create_event(event_create=event_create)


@router.post("/participant", response_model=ParticipantCreateResponse)
def add_participant(participant_in: ParticipantCreateRequest = Body(...)) -> ParticipantCreateResponse:
    return EventService().add_participant(participant_create_request=participant_in)


@router.delete("/")
def delete_participant():
    ...
    # 유저 본인의 참여만 삭제할 수 있다.


@router.delete("/{event_id}", response_model=Event)
def delete_event(
        username: str = Depends(get_username_of_current_user),
) -> Event:
    ...
    # 이벤트 생성자와 삭제 요청 유저가 같은지 확인 후 삭제.


@router.put("/{event_id}", response_model=Event)
def update_event() -> Event:
    ...
    # 이벤트 생성자와 업데이트 요청 유저가 같은지 확인 후 업데이트
