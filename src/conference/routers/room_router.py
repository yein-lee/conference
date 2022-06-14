from fastapi import APIRouter, Depends, Body
from conference.routers.auth_dep import get_username_of_current_user
from conference.services.room_service import RoomService
from conference.schemas.room_schema import Room, RoomCreate

router = APIRouter(dependencies=[Depends(get_username_of_current_user)])


@router.post("/room", response_model=Room)
def create_room(room_in: RoomCreate = Body(...)) -> Room:
    return RoomService().create_room(room_create=room_in)
