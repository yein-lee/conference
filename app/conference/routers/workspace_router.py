from fastapi import APIRouter, Depends, Body, Query
from conference.routers.auth_dep import get_username_of_current_user
from conference.services.workspace_service import WorkspaceService
from conference.schemas.workspace_schema import WorkspaceCreateDTO, WorkspaceWithOwnerIdDTO
from conference.schemas.team_schema import TeamAcceptDTO

router = APIRouter(dependencies=[Depends(get_username_of_current_user)])


@router.post("/", response_model=WorkspaceWithOwnerIdDTO)
async def create_workspace(
        username: str = Depends(get_username_of_current_user),
        workspace_in: WorkspaceCreateDTO = Body(...)
) -> WorkspaceWithOwnerIdDTO:
    return await WorkspaceService.\
        create_workspace_and_map_user(username=username, workspace_create=workspace_in)


@router.get("/")
async def retrieve_workspace_including_name(
        workspace_name_in: str = Query(...)
):
    return await WorkspaceService.\
        retrieve_workspace_including_name(workspace_name=workspace_name_in)


@router.get("/users")
async def get_users_of_workspace(
        username: str = Depends(get_username_of_current_user),
        workspace_id: int = Query(...)
):
    await WorkspaceService.check_team_exists(username=username, workspace_id=workspace_id)
    return await WorkspaceService.get_users_of_workspace(workspace_id=workspace_id)


@router.post("/join")
async def join_workspace(
        username: str = Depends(get_username_of_current_user),
        workspace_id: int = Body(...)
):
    return await WorkspaceService.join_workspace(workspace_id=workspace_id, username=username)


@router.post("/join/accept")
async def accept_join_workspace(
        username: str = Depends(get_username_of_current_user),
        team_accept: TeamAcceptDTO = Body(...)
):
    await WorkspaceService.check_is_owner(workspace_id=TeamAcceptDTO.workspace_id, username=username)
    return await WorkspaceService.accept_join_workspace(team_accept=team_accept)


@router.post("/join/reject")
async def accept_join_workspace(
        username: str = Depends(get_username_of_current_user),
        team_accept: TeamAcceptDTO = Body(...)
):
    await WorkspaceService.check_is_owner(workspace_id=TeamAcceptDTO.workspace_id, username=username)
    return await WorkspaceService.reject_join_workspace(team_accept=team_accept)
