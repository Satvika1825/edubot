from pydantic import BaseModel

class AgentInput(BaseModel):
    subject: str
    topic: str
