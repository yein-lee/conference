from conference.models.workspace_model import Workspace as WorkspaceModel
from conference.schemas.workspace_schema import WorkspaceCreate, WorkspaceWithUserId
from conference.schemas.team_schema import TeamCreate
from conference.repositories.workspace_repo import WorkspaceRepo
from conference.services.user_service import UserService
from conference.services.team_service import TeamService
from conference.schemas.user_schema import UserLevel
from utils.http_exceptions import DuplicationException


class WorkspaceService:
    @classmethod
    def create_workspace(cls, workspace_create: WorkspaceCreate) -> WorkspaceModel:
        exists = WorkspaceRepo().check_workspace_exists_by_name(workspace_create=workspace_create)
        if exists:
            raise DuplicationException(detail="name")
        return WorkspaceRepo().create(workspace_create)

    @classmethod
    def create_workspace_and_map_user(cls, username: str, workspace_create: WorkspaceCreate) \
            -> WorkspaceWithUserId:
        workspace_model = WorkspaceService().create_workspace(workspace_create=workspace_create)
        current_user_model = UserService().get_user_by_username(username=username)
        team_create_schema = TeamCreate(workspace_id=workspace_model.id, user_id=current_user_model.id, user_level=UserLevel.owner)
        team_model = TeamService().create_team(team_create_schema)
        return WorkspaceWithUserId(**workspace_model.__dict__, **team_model.__dict__)

    @classmethod
    def retrieve_workspace_by_name(cls, workspace_name: str):
        ...
