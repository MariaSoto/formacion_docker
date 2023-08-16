from typing import List

import pandas as pd
from schemas import tables_schemas
from configuration import logger
from src.database import connection
from  datetime import datetime
import sqlalchemy as db
from sqlalchemy.exc import NoSuchTableError
# from models import models
from src import responses
from fastapi import UploadFile, File
from io import BytesIO
from models import models as models

# Recreate all 
def recreate_all(database="destinations_clients"):
    
    try: 
        Base = models.Base
        engine, SessionLocal = connection.connection_db_raw(database)
       
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)      
        return responses.response_success()
    except Exception as e:
        logger.info(e)
        return responses.response_fails("e")

# Drop one table
def drop_table(mytable:str):     

    try:
        table, connect, engine = connection.connection_db("destinations_clients",table_name=mytable)
        table.drop(engine)        
        return responses.response_success()

    except Exception as e:
        return responses.response_fails("e")

#Inserting Data--------------------

def inserting_data(table, values_list: list, database:str="destinations_clients"):
    try:
        cpu_time = datetime.now()
        table, connect, engine = connection.connection_db(database, table_name=table)
        query = db.insert(table) 
        # connect.execute("SET SESSION  net_read_timeout = 60000")        
        ResultProxy = connect.execute(query, values_list)
        ResultProxy.close()
        connect.close()
        engine.dispose()
        cpu_time = datetime.now() - cpu_time
        database=''
        logger.info(f"Cpu time spent to insert {len(values_list)} row database {database} : {cpu_time}")
        return True, "ok"
    except Exception as e:
        logger.error(f"Exception: {e}")
        x=input()
        return False, e
    
async def uploadFile_file(table:str, file: UploadFile = File(...)):
    type_file = file.content_type
    
    if type_file != "text/csv": 
        return responses.response_fails("Bad extension")
    
    df_data = read_csv_upload_file(file) 
    df_dict = df_data.to_dict("records")    
    status, msg = inserting_data(table, df_dict)

    return responses.response_success() if status else responses.response_fails(msg)
        
def read_csv_upload_file(file:UploadFile):
    contents = file.file.read()
    buffer = BytesIO(contents)
    df = pd.read_csv(buffer)
      
    buffer.close()
    file.file.close()

    return df

#Update cdr

#Update
def update_cdr( cdr_info:tables_schemas.Maniterm, tableName:str="destinations_clients", database:str="destinations_clients"):
    try:
        cpu_time = datetime.now()        
        #connetion to data_base
        table, connect, engine = connection.connection_db(database,table_name=tableName)
        unique_id = cdr_info.uniqueid
        cdr_info =  cdr_info.dict()
        
        values_dict =  {field:cdr_info[field] for field in cdr_info.keys() if field != "uniqueid" and cdr_info[field] != None}
            
                
        query = db.update(table).where(table.columns.uniqueid == unique_id).values(values_dict)

        ResultProxy = connect.execute(query)        
        ResultProxy.close()
        connect.close()
        engine.dispose()
        cpu_time = datetime.now() - cpu_time        
        return True, "ok"
    except NoSuchTableError as e:
        msg = f"Error connecting with table {e}. Please verify that this table exists"
        return False, msg
    except Exception as e:
        msg = f"Error connecting with table {e}."
        return False, msg
    
# Delete data by unique_id
def delete_cdr(unique_id:str, tableName:str="destinations_clients", database:str="destinations_clients"):
    try:
        #connetion to data_base
        table, connect, engine = connection.connection_db(database,table_name=tableName)
        query = db.delete(table)
        #delete calldate
        query = query.where(table.columns.uniqueid == unique_id)
        
        
        ResultProxy = connect.execute(query)
        
        ResultProxy.close()
        connect.close()
        engine.dispose()
        return responses.response_success()

    except NoSuchTableError as e:
        msg = f"Error connecting with table {e}. Please verify that this table exists"
        return responses.response_fails(msg) 
    except Exception as e:
        msg = f"Error connecting with table {e}."
        return responses.response_fails(msg)

#Read---
def read_by_uniqueid(uniqueid_list:[str], tableName:str="destinations_clients", database:str="destinations_clients"):
    try:
        #connetion to data_base
        table, connect, engine = connection.connection_db(database, table_name=tableName)
        
        #get colunmns to display                
        selected_columns = []
        get_columns = table.columns.keys()
        # get_columns.remove("calldate")
        for var in get_columns:
            selected_columns.append(table.columns[var])
        
        #query
        logger.info(uniqueid_list)
        query = db.select(selected_columns)
        query = query.where(table.columns.uniqueid.in_(uniqueid_list))

        #Order by
        query = query.order_by(table.columns.calldate)

        ResultProxy = connect.execute(query)
        ResultSet = ResultProxy.fetchall()        
        ResultProxy.close()
        connect.close()
        engine.dispose()        
        return True, ResultSet

    except NoSuchTableError as e:
        msg = f"Error connecting with table {e}. Please verify that this table exists"
        return False, msg
    except Exception as e:
        msg = f"Error connecting with table {e}."
        return False, msg
