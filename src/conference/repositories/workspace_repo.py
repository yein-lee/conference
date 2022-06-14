from typing import List
from conference.models.workspace_model import WorkspaceModel
from conference.schemas.workspace_schema import WorkspaceCreate


class WorkspaceRepo:
    @classmethod
    async def check_workspace_exists_by_name(cls, workspace_create: WorkspaceCreate) -> bool:
        exists = await WorkspaceModel.objects.filter(name__exact=workspace_create.name).exists()
        return exists

    @classmethod
    async def create_workspace(cls, workspace_create: WorkspaceCreate) -> WorkspaceModel:
        workspace_model = await WorkspaceModel.objects.create(**workspace_create.__dict__)
        return workspace_model

    @classmethod
    async def retrieve_workspace_including_name(cls, workspace_name: str) -> List[WorkspaceModel]:
        workspace_model_list = await WorkspaceModel.objects.filter(name__contains=workspace_name).all()
        return workspace_model_list
