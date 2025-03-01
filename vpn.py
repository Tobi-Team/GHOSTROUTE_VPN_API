#!/usr/bin/env python3

import uvicorn
import VPN

if __name__ == "__main__":
    config = uvicorn.Config("VPN:app", port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
