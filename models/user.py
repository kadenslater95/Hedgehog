from pydantic import BaseModel, UUID4


class User(BaseModel):
    email: str
    id: UUID4
