from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from conference.routers.router import api_router
from config.db_session import database
from config.settings import Settings

from config.db_session import DATABASE_URL, metadata
from sqlalchemy import create_engine



app = FastAPI()

app.state.database = database

if Settings().BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in Settings().BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router)


@app.on_event("startup")
async def startup() -> None:
    await database.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await database.disconnect()

#
# engine = create_engine(DATABASE_URL)
# metadata.drop_all(engine)
# metadata.create_all(engine)
