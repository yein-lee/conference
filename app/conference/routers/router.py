from fastapi import APIRouter
from conference.routers import login_router, user_router, workspace_router, team_router

api_router: APIRouter = APIRouter()
api_router.include_router(login_router.router, tags=["login"])
api_router.include_router(user_router.router, prefix="/users", tags=["users"])
api_router.include_router(workspace_router.router, prefix="/workspaces", tags=["workspaces"])
api_router.include_router(team_router.router, prefix="/team", tags=["team"])
