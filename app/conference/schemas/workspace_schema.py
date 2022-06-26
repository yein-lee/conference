from conference.schemas.base_schema import BaseSchema


class Workspace(BaseSchema):
    name: str


class WorkspaceCreate(Workspace):
    ...


class WorkspaceWithOwnerId(BaseSchema):
    id: int
    name: str
    owner_id: int
