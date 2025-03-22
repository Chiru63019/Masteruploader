import os

class Config(object):
    BOT_TOKEN = ""
    API_ID = 
    API_HASH = ""
    AUTH_USER = os.environ.get('AUTH_USERS', '').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://api.masterapi.tech"
    CREDIT = ""
