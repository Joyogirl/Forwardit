#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 18038587))
    API_HASH = os.environ.get("API_HASH", "be2d55f7c7a0dec95eea43bf5e0a152a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5120294133:AAEcP25J7OlfNjnBet0MyGfYi4JVwTCbyyE") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "gfgfggffgfgfg")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "-1001708578371")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("OWNER_ID", "1786672678")
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "BQBu2-ce7HamyOpp7_qquQvtGZJJNsgu93-zSa-nAbvB3Jv8Gztmng2KHLo_dzV0gBXS9b1HnA5l9dCPFaR1lWUs4O2XskWbRdlERp1T9dfeJQVkhEyA2ErWc2Eql_WWc5VBLSmBfbbmfBbiIDJgFE19GHNH_Jf3BFYdbVVk5VFpw6zGNM-2DZ-Y7cGDVJ_Tx-Yove6MUTRwH5LR8PVv5clBGgi13t7wMNbWfpyeFBDKMFIOpfeqQfkMEQjHYYzXd0z4uI5BdA525oFFukIVLb7J3ZjUy0GqV_Msamq4eq_d8PwARtJqZ9PlBVE6k_wlBZQ-ggQpkJT4AD8Yfnukdq83an52JgA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001510870866"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
