from typing import List
from conference.models.workspace_model import WorkspaceModel
from conference.models.team_model import TeamModel
from conference.schemas.workspace_schema import WorkspaceCreate, WorkspaceWithOwnerId
from conference.schemas.team_schema import TeamCreate
from conference.repositories.workspace_repo import WorkspaceRepo
from conference.services.user_service import UserService
from conference.services.team_service import TeamService
from conference.schemas.team_schema import TeamAccept
from conference.schemas.user_schema import UserLevel
from utils.http_exceptions import DuplicationException, NotFoundException, PermissionException


class WorkspaceService:
    @classmethod
    async def create_workspace(cls, workspace_create: WorkspaceCreate) -> WorkspaceModel:
        exists = await WorkspaceRepo().check_workspace_exists_by_name(workspace_create=workspace_create)
        if exists:
            raise DuplicationException(detail="name")
        return await WorkspaceRepo().create_workspace(workspace_create)

    @classmethod
    async def retrieve_workspace_including_name(cls, workspace_name: str) -> List[WorkspaceModel]:
        return await WorkspaceRepo().retrieve_workspace_including_name(workspace_name=workspace_name)

    @classmethod
    async def create_workspace_and_map_user(cls, username: str, workspace_create: WorkspaceCreate) \
            -> WorkspaceWithOwnerId:
        user_model = await UserService().get_user_by_username(username=username)
        workspace_model = await WorkspaceRepo().create_workspace_and_map_user(
            workspace_create=workspace_create, user=user_model)
        workspace_with_owner_id = WorkspaceWithOwnerId(
            id=workspace_model.id,
            name=workspace_model.name,
            owner_id=user_model.id
        )
        return workspace_with_owner_id

    @classmethod
    async def join_workspace(cls, workspace_id: int, username: str) -> TeamModel:
        workspace_model = await WorkspaceRepo().get_workspace_by_id(workspace_id=workspace_id)
        if workspace_model is None:
            raise NotFoundException(detail="workspace")
        user_model = await UserService().get_user_by_username(username=username)
        team_create_schema = TeamCreate(
            workspace_id=workspace_model.id,
            user_id=user_model.id,
            user_level=UserLevel.member,
            accepted=False
        )
        return await TeamService().create_team(team_create_schema)

    @classmethod
    async def get_users_of_workspace(cls, workspace_id: int):
        return await WorkspaceRepo().get_users_of_workspace(workspace_id=workspace_id)

    @classmethod
    async def check_is_team(cls, workspace_id: int, username: str) -> bool:
        return await UserService().check_is_team(username=username, workspace_id=workspace_id)

    @classmethod
    async def check_is_owner(cls, workspace_id: int, username: str) -> bool:
        user_with_team_model = await UserService().get_user_with_team(username=username, workspace_id=workspace_id)
        if user_with_team_model.teammodel.user_level is not UserLevel.owner:
            raise PermissionException()
        return True

    @classmethod
    async def accept_join_workspace(cls, team_accept: TeamAccept) -> TeamModel:
        return await TeamService().accept_join_workspace(team_accept=team_accept)

    @classmethod
    async def reject_join_workspace(cls, team_accept: TeamAccept) -> TeamModel:
        return await TeamService().reject_join_workspace(team_accept=team_accept)