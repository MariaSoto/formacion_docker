from email import message
from pydantic import BaseModel
from typing import Optional

class Response(BaseModel):    
    status: bool = None
    message: Optional[str] = None
    cpu_time: Optional[str] = None
    data: Optional[dict] = None


class Message(BaseModel):
    message: str

code400 = {
    400: {"model": Message}
}
code401 = {
    401: {"model": Message}
}
code403 = {
    403: {"model": Message}
}
code404 = {
    404: {"model": Message}
}

codeAll = {
    400: {"model": Message},
    401: {"model": Message},
    403: {"model": Message},
    404: {"model": Message}
}
