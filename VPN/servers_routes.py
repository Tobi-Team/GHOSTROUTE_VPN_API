from VPN import app
from fastapi import status, Depends, HTTPException, Form

# get all servers
# get all private servers + 100% anonymity + 98%+ speed + 99.99% privacy
# get all public servers + 90%+ speed 


@app.get("/server/get_all_servers", status_code=status.HTTP_200_OK)
@app.get("/server/get_all_servers/", status_code=status.HTTP_200_OK)
def get_all_servers():
    # To return lists of all servers
