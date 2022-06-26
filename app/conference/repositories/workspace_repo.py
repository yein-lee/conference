from typing import List, Optional
from config.db_session import database
from conference.models.workspace_model import WorkspaceModel
from conference.models.team_model import TeamModel
from conference.models.user_model import UserModel
from conference.schemas.team_schema import TeamCreate
from conference.schemas.user_schema import UserLevel
from conference.schemas.workspace_schema import WorkspaceCreate


class WorkspaceRepo:
    @classmethod
    async def get_workspace_by_id(cls, workspace_id: int) -> Optional[WorkspaceModel]:
        return await WorkspaceModel.objects.get(id=workspace_id)

    @classmethod
    async def check_workspace_exists_by_name(cls, workspace_create: WorkspaceCreate) -> bool:
        return await WorkspaceModel.objects.filter(name__exact=workspace_create.name).exists()

    @classmethod
    async def create_workspace(cls, workspace_create: WorkspaceCreate) -> WorkspaceModel:
        return await WorkspaceModel.objects.create(**workspace_create.__dict__)

    @classmethod
    async def retrieve_workspace_including_name(cls, workspace_name: str) -> List[WorkspaceModel]:
        return await WorkspaceModel.objects.filter(name__contains=workspace_name).all()

    @classmethod
    async def get_users_of_workspace(cls, workspace_id: int):
        return await WorkspaceModel.objects.select_related(WorkspaceModel.teammodels.user_id).get(id=workspace_id)

    @classmethod
    @database.transaction()
    async def create_workspace_and_map_user(cls, workspace_create: WorkspaceCreate, user: UserModel) -> WorkspaceModel:
        workspace_model = await WorkspaceModel(**workspace_create.__dict__).save()
        team_create = TeamCreate(
            workspace_id=workspace_model.id,
            user_id=user.id,
            user_level=UserLevel.owner,
            accepted=True
        )
        await TeamModel(**team_create.__dict__).save()
        return workspace_model
