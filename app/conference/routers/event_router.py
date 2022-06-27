from fastapi import APIRouter, Depends, Body, Path
from conference.routers.auth_dep import get_username_of_current_user
from conference.services.event_service import EventService
from conference.services.workspace_service import WorkspaceService
from conference.schemas.event_schema import EventCreate, EventUpdate

router = APIRouter(dependencies=[Depends(get_username_of_current_user)])


@router.post("/")
async def create_event(
        username: str = Depends(get_username_of_current_user),
        workspace_id: int = Path(...),
        room_id: int = Path(...),
        event_in: EventCreate = Body(...)
):
    await WorkspaceService().check_is_owner_or_member(workspace_id=workspace_id, username=username)
    return await EventService().create_event(event_create=event_in)


@router.post("/")
async def update_event(
        username: str = Depends(get_username_of_current_user),
        workspace_id: int = Path(...),
        room_id: int = Path(...),
        event_in: EventUpdate = Body(...)
):
    await WorkspaceService().check_is_owner_or_member(workspace_id=workspace_id, username=username)
    return await EventService().update_event(event_update=event_in)
