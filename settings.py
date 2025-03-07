import configparser

config = configparser.ConfigParser()
config.read("config.ini")

api_id = int(config["pyrogram"]["api_id"])
api_hash = config["pyrogram"]["api_hash"]
session_name = "my_session"

chats_id = {
    # Примеры:
    -4703732482: -4696004023,
    (-1002386828463, "General"): -4696004023,
}
