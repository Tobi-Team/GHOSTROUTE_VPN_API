from VPN import app
from fastapi import status, Depends, HTTPException, Form


from VPN.pydantic_models import (
    select_server_type
)
from VPN.vpn_misc import (
    SERVER_LIST, SERVER_DICT
)

# get all servers
# get all private servers + 100% anonymity + 98%+ speed + 99.99% privacy
# get all public servers + 90%+ speed 


@app.post("/server/get_all_servers", status_code=status.HTTP_200_OK)
@app.post("/server/get_all_servers/", status_code=status.HTTP_200_OK)
def get_all_servers(data: select_server_type):
    server_list = SERVER_LIST
    server_obj = SERVER_DICT

    server_list_return = []
    server_obj_return = {}
    if (data.server_type is None) or (data.server_type == ""):
        try:
            for item in server_list:
                if item in server_obj:
                    # if item if found, apend to list and add to object
                    server_list_return.append(item)
                    server_obj_return[item] = server_obj[item]
        except Exception as e:
            raise
            raise HTTPException(status_code=500, detail={"err": str(e)})
    elif data.server_type == "public":
        try:
            for item in server_list:
                if (item in server_obj) and (server_obj[item]["type"] == "public"):
                    server_list_return.append(item)
                    server_obj_return[item] = server_obj[item]
        except Exception as e:
            raise
            raise HTTPException(status_code=500, detail={"err": str(e)})
    elif data.server_type == "private":
        try:
            for item in server_list:
                if (item in server_obj) and (server_obj[item]["type"] == "private"):
                    server_list_return.append(item)
                    server_obj_return[item] = server_obj[item]
        except Exception as e:
            raise
            raise HTTPException(status_code=500, detail={"err": str(e)})
    return {
        "statusCode": 200,
        "status": True,
        "message": "success",
        "data": {
            "servers": server_list_return,
            "servers_info": server_obj_return
        }
    }
    # To return lists of all servers
