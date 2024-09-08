class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5675252446"
    sudo_users = "5675252446"
    GROUP_ID = -1001926606886
    TOKEN = "6629091452:AAGva53lk8QbOQ46qCiPE1HyEwi0alktHds"
    mongo_url = "mongodb+srv://yunyxedits:assalom%4013@waifudata.vfutysm.mongodb.net/?retryWrites=true&w=majority&appName=waifudata"
    PHOTO_URL = ["https://ibb.co/q7jzMwz", "https://ibb.co/T2qNx5m", "https://ibb.co/TYS7yC4", "https://ibb.co/hVRR0T1", "https://ibb.co/3W3rVy6"]
    SUPPORT_CHAT = "Aniverse_Group"
    UPDATE_CHAT = "Aniverse_Group"
    BOT_USERNAME = "LOVETHETICX_bot"
    CHARA_CHANNEL_ID = "-1001926606886"
    api_id = 29668491
    api_hash = "84feb2e86bc3fa3b0b9bc1e3a3428177"

    STRICT_GBAN = True
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
