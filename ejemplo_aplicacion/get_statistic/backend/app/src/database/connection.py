

from sqlalchemy import create_engine
import sqlalchemy as db
import json
from server import settings, logger
from sqlalchemy.orm import sessionmaker

# Session
SessionLocal = None
Engine = None 


def connection_db_raw(profil:str):
    data = get_access_db(profil)
    host_url = settings.hostdb_uri
    database_uri = f"{data['dialect']}+{data['driver']}://{data['user']}:{data['password']}@{host_url}/{data['database']}"    
    Engine = create_engine(database_uri)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
    return Engine, SessionLocal

def connection_db(profil:str, table_name=None):    
    data = get_access_db(profil)      

    Engine, sess = connection_db_raw(profil)#create_engine(database_uri)
    connection = Engine.connect()
    metadata = db.MetaData()
    table_db = data['table']
    if table_name != None: table_db = table_name
    
    table = db.Table(table_db, metadata, autoload=True, autoload_with=Engine)
    return table, connection, Engine
     
def get_access_db(profil):
    file_access_db = settings.file_access_db
    with open(file_access_db, "r") as f: 
        data = json.loads(f.read())
        return data[profil]
