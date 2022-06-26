from ormar import Model, Integer, ForeignKey, Enum, Boolean
from conference.models.base_model import BaseMeta
from conference.models.workspace_model import WorkspaceModel
from conference.models.user_model import UserModel
from conference.schemas.user_schema import UserLevel


class TeamModel(Model):
    class Meta(BaseMeta):
        tablename = "team"

    id: int = Integer(primary_key=True, index=True)
    workspace_id: WorkspaceModel = ForeignKey(WorkspaceModel)
    user_id: int = ForeignKey(UserModel)
    user_level: str = Enum(enum_class=UserLevel)
    accepted: bool = Boolean(nullable=True)
