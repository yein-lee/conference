from conference.models.workspace_model import WorkspaceModel
from conference.schemas.workspace_schema import WorkspaceCreate, WorkspaceWithUserId
from conference.schemas.team_schema import TeamCreate
from conference.repositories.workspace_repo import WorkspaceRepo
from conference.services.user_service import UserService
from conference.schemas.user_schema import UserLevel
from utils.http_exceptions import DuplicationException


class WorkspaceService:
    @classmethod
    async def create_workspace(cls, workspace_create: WorkspaceCreate) -> WorkspaceModel:
        exists = await WorkspaceRepo().check_workspace_exists_by_name(workspace_create=workspace_create)
        if exists:
            raise DuplicationException(detail="name")
        return await WorkspaceRepo().create_workspace(workspace_create)

    @classmethod
    def retrieve_workspace_by_name(cls, workspace_name: str):
        ...
