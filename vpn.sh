#!/usr/bin/env bash

source vpn_env/bin/activate
pip install -r requirements.txt
uvicorn VPN:app --reload
