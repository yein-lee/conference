from conference.schemas.base_schema import BaseSchema
from conference.schemas.user_schema import UserLevel


class Team(BaseSchema):
    workspace_id: int
    user_id: int


class TeamCreateDTO(BaseSchema):
    workspace_id: int
    user_id: int
    user_level: UserLevel
    accepted: bool


class TeamAcceptDTO(BaseSchema):
    workspace_id: int
    user_id: int


class TeamExistDTO(BaseSchema):
    workspace_id: int
    user_id: int
