from pydantic import BaseModel, Extra


class BaseSchema(BaseModel):
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        extra = Extra.ignore
