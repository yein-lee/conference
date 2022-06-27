from conference.models.team_model import TeamModel
from conference.schemas.team_schema import TeamCreateDTO, TeamExistDTO, TeamAcceptDTO


class TeamRepo:
    @classmethod
    async def check_team_exists_by_workspace_id_and_user_id(cls, team_exist: TeamExistDTO) -> bool:
        exists = await TeamModel.objects.filter(
            workspace_id__exact=team_exist.workspace_id,
            user_id__exact=team_exist.user_id
        ).exists()
        return exists

    @classmethod
    async def create(cls, team_create: TeamCreateDTO) -> TeamModel:
        team_model = await TeamModel.objects.create(**team_create.__dict__)
        return team_model

    @classmethod
    async def get_team_by_workspace_id_and_user_id(cls, team_exist: TeamExistDTO):
        team_model = await TeamModel.objects.get(workspace_id=team_exist.workspace_id, user_id=team_exist.user_id)
        return team_model

    @classmethod
    async def accept(cls, team_accept: TeamAcceptDTO) -> TeamModel:
        team_model = await TeamModel.objects.get(workspace_id=team_accept.workspace_id, user_id=team_accept.user_id)
        await team_model.update(accepted=True)
        return team_model

    @classmethod
    async def reject(cls, team_accept: TeamAcceptDTO) -> TeamModel:
        team_model = await TeamModel.objects.get(workspace_id=team_accept.workspace_id, user_id=team_accept.user_id)
        await team_model.update(accepted=False)
        return team_model
