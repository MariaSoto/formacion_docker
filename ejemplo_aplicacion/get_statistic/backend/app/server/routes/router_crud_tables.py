from schemas import tables_schemas
from fastapi import APIRouter, UploadFile, File
from typing import List
from schemas import  responses_schemas
from src.database import crud_tables as crud
from src import responses

router = APIRouter()

#CRUD ----------------
# Create/insert a row in table
@router.post("/database/add_cdr",  tags=["Create"], response_model=responses_schemas.Response)
def add_table(table_name:str, data: List[tables_schemas.Maniterm]):    
    data_dict = [ x.dict() for x in data ]
    status, msg = crud.inserting_data(table_name, data_dict)
    return responses.response_success() if status else responses.response_fails(msg)

# Read data from table
@router.post("/database/read_cdr", tags=["Read"],response_model=responses_schemas.Response)
def read_cdr(uniqueids: List[str]):
	status, res = crud.read_by_uniqueid(uniqueids)
	return responses.response_success(mydata={"res":res}) if status else responses.response_fails(res)

#Update data
@router.post("/database/update_cdr",  tags=["Update"], response_model=responses_schemas.Response)
def update_cdr(cdr_info:tables_schemas.Maniterm):
	status, msg = crud.update_cdr(cdr_info)
	return responses.response_success() if status else responses.response_fails(msg)

#Delete data from table
@router.delete("/database/delete_cdr", tags=["Delete"], response_model=responses_schemas.Response) 
def delete_data_by_id_unique(id_unique:str):
	return crud.delete_cdr(id_unique)
#-------------------------

# Create all tables
@router.get("/database/recreate_all/destinations_clients", tags=["Set tables"], response_model=responses_schemas.Response) #responses={**responsesSchemas.codeAll},
def recreate_all():
	return crud.recreate_all()

#Upload data
@router.post("/database/uploadfile_cdr", tags=["Upload data"])#, response_model=responses_schemas.Response)
async def uploadfile_data(table_name:str, file: UploadFile = File(...)):#, client:str=Form(), campaign:str=Form(), date_study:str=Form(),period_time_days:str=Form()):
	return await crud.uploadFile_file(table_name, file)

#Drop a table
@router.delete("/database/drop_table/", tags=["Drop"],  response_model=responses_schemas.Response)
def drop_table(table:str):
	return  crud.drop_table(table)
