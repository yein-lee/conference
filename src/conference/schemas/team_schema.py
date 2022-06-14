from conference.schemas.base_schema import BaseSchema
from conference.schemas.user_schema import UserLevel


class Team(BaseSchema):
    workspace_id: int
    user_id: int


class TeamCreate(Team):
    user_level: UserLevel


class TeamExist(Team):
    ...
