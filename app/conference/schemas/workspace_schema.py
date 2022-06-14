from conference.schemas.base_schema import BaseSchema


class Workspace(BaseSchema):
    name: str


class WorkspaceCreate(Workspace):
    ...


class WorkspaceWithUserId(BaseSchema):
    id: int
    name: str
    user_id: int
