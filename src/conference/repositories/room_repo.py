from conference.models.room_model import RoomModel
from conference.schemas.room_schema import RoomCreate


class RoomRepo:
    @classmethod
    def check_room_exists_by_workspace_id_and_name(cls, room_create: RoomCreate):
        with SessionLocal() as db:
            exists = db.query(RoomModel).filter(
                db.query(RoomModel).filter(
                    RoomModel.workspace_id == room_create.workspace_id,
                    RoomModel.name == room_create.name).exists()
            ).scalar()
        return exists

    @classmethod
    def create_room(cls, room_create: RoomCreate) -> RoomModel:
        room_model = RoomModel(**room_create.dict())
        with SessionLocal() as db:
            db.add(room_model)
            db.commit()
            db.refresh(room_model)
        return room_model
