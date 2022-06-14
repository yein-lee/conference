from conference.models.team_model import TeamModel
from conference.schemas.team_schema import TeamCreate, TeamExist


class TeamRepo:
    @classmethod
    def check_team_exists_by_workspace_id_and_name(cls, team_exist: TeamExist):
        with SessionLocal() as db:
            exists = db.query(TeamModel).filter(
                db.query(TeamModel).filter(
                    TeamModel.workspace_id == team_exist.workspace_id,
                    TeamModel.user_id == team_exist.user_id).exists()
            ).scalar()
        return exists

    @classmethod
    def create(cls, team_create: TeamCreate) -> TeamModel:
        team_model = TeamModel(**team_create.dict())
        with SessionLocal() as db:
            db.add(team_model)
            db.commit()
            db.refresh(team_model)
        return team_model
