import configparser

config = configparser.ConfigParser()
config.read("config.ini")

api_id = int(config["pyrogram"]["api_id"])
api_hash = config["pyrogram"]["api_hash"]
session_name = "my_session"

#format ====> source_chat : target_chat
chats_id = {
    -4703732482 : -4696004023,
}
