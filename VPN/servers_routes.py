from VPN import app
from fastapi import status, Depends, HTTPException, Form


from VPN.pydantic_models import (
    ip_pydantic
)
from VPN.vpn_misc import (
    SERVER_LIST, SERVER_DICT
)

import httpx
from httpx import Timeout

# get all servers
# get all private servers + 100% anonymity + 98%+ speed + 99.99% privacy
# get all public servers + 90%+ speed 


@app.post("/server/get_all_servers/{server_type}", status_code=status.HTTP_200_OK, tags=["SERVERS"])
@app.post("/server/get_all_servers/{server_type}/", status_code=status.HTTP_200_OK, tags=["SERVERS"])
def get_all_servers(server_type: str):
    """
    To return a list of all servers
    along with their basic information!
    """
    server_list, server_obj = (SERVER_LIST, SERVER_DICT)

    if (not server_type) or (server_type == "") or (server_type == "\"\""):
        server_type = None

    server_list_return = []
    server_obj_return = {}
    if (server_type is None):
        try:
            for item in server_list:
                if item in server_obj:
                    # if item if found, apend to list and add to object
                    server_list_return.append(item)
                    server_obj_return[item] = server_obj[item]
        except Exception as e:
            raise
            raise HTTPException(status_code=500, detail={"err": str(e)})
    elif server_type == "public":
        try:
            for item in server_list:
                if (item in server_obj) and (server_obj[item]["type"] == "public"):
                    server_list_return.append(item)
                    server_obj_return[item] = server_obj[item]
        except Exception as e:
            raise
            raise HTTPException(status_code=500, detail={"err": str(e)})
    elif server_type == "private":
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



@app.post("/server/new_config", status_code=status.HTTP_200_OK, tags=["SERVERS"])
@app.post("/server/new_config/", status_code=status.HTTP_200_OK, tags=["SERVERS"])
def new_config(data: ip_pydantic):
    """
    To create a new configuration/connection settings
    belonging to a vpn server using it's ip
    """
    ip_address = data.ip_address
    if (not ip_address) or (ip_address == ""):
        ip_address = None
    if ip_address is None:
        raise HTTPException(status_code=400, detail={"err": "Kindly input IP!"})
    if ip_address not in SERVER_LIST:
        raise HTTPException(
            status_code=400,
            detail={"err": "{} does not exist in our dataset!".format(ip_address)}
        )

    server_data = SERVER_DICT[ip_address]
    config_response = (None,)

    # connect to server using httpx and recieve connection data
    try:
        with httpx.Client(timeout=Timeout(50.0)) as client:
            # set timeout to 50 seconds
            response = client.get("http://{server_ip}/create_peer/".format(
                server_ip=ip_address
            ), headers={"Content-Type": "application/json"})
            config_response = response.json()["data"]
    except httpx.TimeoutException as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise

    return {
        "statusCode": 200,
        "status": True,
        "message": "success",
        "data": {
            "ip_address": ip_address,
            "location": server_data.get("location"),
            "type": server_data.get("type"),
            "configuration": {
                "client": config_response.get("client_id"),
                "config": config_response.get("configuration")
            }
        }
    }

    



