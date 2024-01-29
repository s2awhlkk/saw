import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6904017239:AAFWbMgpgNVPYC7NaGAfBJq22gDjZljfPLc")

    APP_ID = int(os.environ.get("APP_ID", 21464763))

    API_HASH = os.environ.get("API_HASH", "a382076af5932aa48f3430c8693be11d")