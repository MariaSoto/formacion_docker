
from schemas import responses_schemas
from configuration import logger

#  Reponses
def response_success(my_message = "Success", my_cpu_time:str=None, mydata:dict=None):
    return responses_schemas.Response(
        status = True,
        message = my_message,
        cpu_time = str(my_cpu_time),
        data = mydata )

def response_fails(e):
    logger.error(e)
    return responses_schemas.Response(status = False, message = e)

