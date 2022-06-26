from conference.schemas.team_schema import TeamCreate, TeamExist, TeamAccept
from conference.models.team_model import TeamModel
from conference.repositories.team_repo import TeamRepo
from utils.http_exceptions import DuplicationException, NotFoundException


class TeamService:
    @classmethod
    async def create_team(cls, team_create: TeamCreate) -> TeamModel:
        team_exist = TeamExist(**team_create.__dict__)
        exists = await TeamRepo().check_team_exists_by_workspace_id_and_user_id(team_exist=team_exist)
        if exists:
            raise DuplicationException(detail="team")
        return await TeamRepo().create(team_create=team_create)

    @classmethod
    async def check_team_exists(cls, team_exist: TeamExist) -> bool:
        exists = await TeamRepo().check_team_exists_by_workspace_id_and_user_id(team_exist=team_exist)
        if not exists:
            raise NotFoundException(detail="team")
        return True

    @classmethod
    async def accept_join_workspace(cls, team_accept: TeamAccept) -> TeamModel:
        return await TeamRepo().accept(team_accept)

    @classmethod
    async def reject_join_workspace(cls, team_accept: TeamAccept) -> TeamModel:
        return await TeamRepo().reject(team_accept)
