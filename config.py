from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "ebb06ea8d41420e60b29140dcee902fc")
      API_ID = int(getenv("API_ID", "27900743"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7933892614:AAEqwI11hizxUS39ThqDXz6-6OxXHD0kmh4")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002660646128:-1002573051124").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
