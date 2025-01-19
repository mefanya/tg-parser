from pyrogram import Client, filters
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

api_id = int(config["pyrogram"]["api_id"])
api_hash = config["pyrogram"]["api_hash"]
session_name = "my_session"

app = Client(session_name, api_id, api_hash)

source_chat = -4703732482
target_chat = -4696004023


# @app.on_message()
# async def get_chat_id(client, message):
#     print(f"Chat ID: {message.chat.id}")  # Выведет ID чата

# app.run()

@app.on_message(filters.chat(source_chat)) 
async def forward_message(client, message):
    try:
        await client.forward_messages(target_chat, message.chat.id, message.id)
    except Exception as e:
        print(f"Error: {e}")

app.run()
