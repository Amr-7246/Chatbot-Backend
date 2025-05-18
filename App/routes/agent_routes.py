from fastapi import APIRouter, Request
from App.controllers.agent_controller import handle_agent_question

agent_router = APIRouter()

@agent_router.post("/")
async def ask_agent(request: Request):
    return await handle_agent_question(request)
