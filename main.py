from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from src.conference.routers.router import api_router
from src.config.db_session import DATABASE_URL, metadata
from src.config.settings import Settings


engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()

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
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()
