import os
from pydantic import BaseSettings
import logging

# global logger
logger = logging.getLogger("manifone")
FORMAT = "%(asctime)-15s: [%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
#logger.setLevel(logging.DeBUG)

class Settings(BaseSettings):
    
    #  server settings
    app_title : str = "Get data"
    version : str = "1.0.0"
    root_path : str = "/"#None
    openapi_prefix : str = ""
    has_static : bool = True

    #  database
    file_access_db = "./configuration/access_db.json"    
    hostdb_uri : str = "db"

    
    def update(self):

        if "ROOT_PATH" in os.environ:
            self.root_path = os.environ["ROOT_PATH"]
        if "FILE_ACCESS_DB" in os.environ:
            self.file_access_db = os.environ["FILE_ACCESS_DB"]
        if "HOSTDB_URI" in os.environ:
            self.hostdb_uri = os.environ["HOSTDB_URI"]
            logger.info(self.hostdb_uri)
    