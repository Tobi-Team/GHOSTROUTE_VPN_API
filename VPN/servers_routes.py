from VPN import app
from fastapi import status, Depends, HTTPException, Form

from VPN.vpn_misc import (
    SERVER_LIST, SERVER_DICT
)

# get all servers
# get all private servers + 100% anonymity + 98%+ speed + 99.99% privacy
# get all public servers + 90%+ speed 


@app.get("/server/get_all_servers", status_code=status.HTTP_200_OK)
@app.get("/server/get_all_servers/", status_code=status.HTTP_200_OK)
def get_all_servers():
    server_list = SERVER_LIST
    server_obj = SERVER_DICT

    server_list_return = []
    server_obj_return = {}
    try:
        for item in server_list:
            if item in server_obj:
                server_list_return.append(item)
                server_obj_return["".format(item)] = server_obj[item]
            else:
                pass
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
