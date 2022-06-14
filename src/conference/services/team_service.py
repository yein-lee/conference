from conference.schemas.team_schema import TeamCreate, TeamExist
from conference.models.team_model import Team as TeamModel
from conference.repositories.team_repo import TeamRepo
from utils.http_exceptions import DuplicationException, NotFoundException


class TeamService:
    @classmethod
    def create_team(cls, team_create: TeamCreate) -> TeamModel:
        exists = TeamRepo().check_team_exists_by_workspace_id_and_name(**team_create.dict())
        if exists:
            raise DuplicationException(detail="team")
        return TeamRepo().create(team_create=team_create)

    @classmethod
    def check_team_exists(cls, team_exist: TeamExist):
        exists = TeamRepo().check_team_exists_by_workspace_id_and_name(team_exist=team_exist)
        if not exists:
            raise NotFoundException(detail="team")
        return True
