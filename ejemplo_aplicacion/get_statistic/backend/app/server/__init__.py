
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from configuration import Settings, logger
import json
# settings
settings = Settings()
logger = logger

description = """
**Get data** is a Python library for requestings databases deployed in local or in a server.
 A *simple* and *intuitive* API is provide here 🚀.
"""

def create_app(settings):    
    app = FastAPI(
        title=settings.app_title,
        description=description, 
        version=settings.version, 
        root_path=settings.root_path,
        docs_url="/documentation", 
        # openapi_prefix=settings.openapi_prefix,        
        redoc_url=None,
        swagger_ui_parameters = {"docExpansion":"none"}
        )

    # Add cors
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    #  routing
    from .routes import router_crud_tables    
    app.include_router(router_crud_tables.router)
    
    return app

def upload_tags():
    directory = './server/docs/'
    files = os.listdir(directory)       
    files.sort()
    
    tags_metadata = []
    for file in files:
        # logger.info(file)
        with open(f"{directory}{file}", "r") as f: 
            data = json.loads(f.read())            
            tags_metadata.extend(data["tags"])
                
    return tags_metadata
