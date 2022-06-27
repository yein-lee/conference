from fastapi import APIRouter, Depends, Body, Path
from conference.routers.auth_dep import get_username_of_current_user
from conference.services.workspace_service import WorkspaceService
from conference.schemas.room_schema import RoomCreate
from conference.services.room_service import RoomService

router = APIRouter(dependencies=[Depends(get_username_of_current_user)])


@router.post("/")
async def create_room(
        username: str = Depends(get_username_of_current_user),
        workspace_id: int = Path(...),
        room_in: RoomCreate = Body(...)
):
    await WorkspaceService.check_is_owner_or_member(workspace_id=workspace_id, username=username)
    return await RoomService.create_room(room_in)
