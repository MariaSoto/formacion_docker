from optparse import Option
from pydantic import BaseModel, validator
from typing import Optional, List
from datetime import date

class Maniterm(BaseModel):
    uniqueid : str
    calldate : Optional[date]    
    destination : Optional[str]
    prefix : Optional[int]
    outcallerid : Optional[str]
    days_last_call : Optional[int]
    diff_seconds : Optional[float]
    disposition : Optional[str]
    billsec : Optional[int]
    duration : Optional[int]
    called_hangup : Optional[int]
    amd:Optional[int]
    npv:Optional[int]
    siren:Optional[int]