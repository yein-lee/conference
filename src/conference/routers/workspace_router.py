from fastapi import APIRouter, Depends, Body, Query
from conference.routers.auth_dep import get_username_of_current_user
from conference.services.workspace_service import WorkspaceService
from conference.schemas.workspace_schema import WorkspaceCreate, WorkspaceWithUserId

router = APIRouter(dependencies=[Depends(get_username_of_current_user)])


@router.post("/", response_model=WorkspaceWithUserId)
def create_workspace(
        username: str = Depends(get_username_of_current_user),
        workspace_in: WorkspaceCreate = Body(...)
) -> WorkspaceWithUserId:
    return WorkspaceService().\
        create_workspace_and_map_user(username=username, workspace_create=workspace_in)


@router.get("/")
def retrieve_workspace(
        workspace_name_in: str = Query(...)
):
    return WorkspaceService().\
        retrieve_workspace_by_name(workspace_name=workspace_name_in)


@router.post("/{workspace_id}")
def join_workspace():
    ...
    # 워크스페이스의 오너에게 조인 요청을 보낸다.
    #


@router.post("/{workspace_id}/accept-join/{user_id}")
def accept_join_workspace_request():
    ...
    # 오너가 accpet 한다.


@router.post("/{workspace_id}/reject-join/{user_id}")
def reject_join_workspace_request():
    ...
    # 오너가 reject 한다.


@router.get("/{workspace_id}/users")
def get_all_users_name_of_workspace():
    ...

