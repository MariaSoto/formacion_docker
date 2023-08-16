### models.py ###
from sqlalchemy import  Column, Integer, BigInteger, String, DateTime, Float, DefaultClause
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Maniterm(Base):
    __tablename__ = 'destinations_clients'    
    id = Column(BigInteger, primary_key=True)
    calldate = Column( DateTime, nullable=False, index=True)
    uniqueid = Column(String(256), nullable=False)
    destination = Column(String(256), nullable=False, index=True)
    prefix = Column(Integer, nullable=False, default=0, index=True)
    outcallerid = Column(String(256), nullable=False, index=True)
    days_last_call = Column(Integer, nullable=True, default=-1, index=True)
    diff_seconds = Column(Float, nullable=False)
    disposition = Column(String(256), nullable=False)
    billsec = Column(Integer, nullable=True)
    duration = Column(Integer, nullable=True)
    called_hangup = Column(TINYINT, nullable=True, default=0)
    amd = Column(TINYINT, nullable=False, server_default="0")
    npv = Column(TINYINT,  DefaultClause("0"), nullable=False)
    siren = Column(Integer, nullable=False, server_default="0", index=True)

    def __repr__(self):
        return f"<destinations_clients(calldate='{self.calldate}', uniqueid='{self.uniqueid}', destination={self.destination}, prefix={self.prefix})>"

