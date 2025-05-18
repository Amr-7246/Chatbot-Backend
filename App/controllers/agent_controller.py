from fastapi import Request
from App.Agent.ai_agent import create_agent
from fastapi.concurrency import run_in_threadpool

agent = create_agent()

async def handle_agent_question(request: Request):
    data = await request.json()
    prompt = data.get("prompt")
    if not prompt:
        return {"error": "No prompt provided"}
    try:
        result = await run_in_threadpool(agent.run, prompt)
        return {"response": result}
    except Exception as e:
        if "credit balance" in str(e).lower():
            return {"error": "Sorry pro . . But my free tiar at AI service run out of credits . . You can visit my github to make suer that my application are built well "}
        return {"error": str(e)}


