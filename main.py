from pyrogram import Client, filters
from settings import api_id, api_hash, session_name, chats_id

app = Client(session_name, api_id, api_hash)

#команда .type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
async def get_chat_id(client, message):
    print(f"Chat ID: {message.chat.id}")

#Функция для пересылки сообщений между чатами
@app.on_message(filters.all)
async def forward_message(client, message):
    try:
        for source_chat, target_chat in chats_id.items():
            if message.chat.id == source_chat:
                await client.forward_messages(target_chat, message.chat.id, message.id)
                break
    except Exception as e:
        print(f"Error: {e}")

app.run()
