from fastapi import APIRouter, Depends, Body, Query, Path
from conference.routers.auth_dep import get_username_of_current_user
from conference.services.team_service import TeamService

router = APIRouter(dependencies=[Depends(get_username_of_current_user)])

