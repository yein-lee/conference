from conference.schemas.base_schema import BaseSchema


class WorkspaceCreateDTO(BaseSchema):
    name: str


class WorkspaceWithOwnerIdDTO(BaseSchema):
    id: int
    name: str
    owner_id: int
