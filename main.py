from pyrogram import Client, filters
from settings import api_id, api_hash, session_name, chats_id

app = Client(session_name, api_id, api_hash)

# Команда .type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
async def get_chat_id(client, message):
    print(f"Chat ID: {message.chat.id}")

@app.on_message(filters.all)
async def copy_message_handler(client, message):
    try:
        for source_chat, target_chat in chats_id.items():
            if message.chat.id == source_chat:
                sender = message.from_user
                hashtag = f"#{sender.first_name}_{sender.last_name}" if sender and sender.first_name else "#Unknown"

                if message.text:
                    await client.send_message(
                        chat_id=target_chat,
                        text=f"{hashtag}\n\n{message.text}"
                    )
                elif message.photo or message.video or message.audio or message.document:
                    caption = f"{hashtag}\n\n{message.caption or 'Прислал медиафайл'}"
                    await client.send_message(
                        chat_id=target_chat,
                        text=caption
                    )
                elif message.sticker:
                    await client.send_message(
                        chat_id=target_chat,
                        text=f"{hashtag}\n\nПрислал стикер"
                    )
                else:
                    await client.send_message(
                        chat_id=target_chat,
                        text=f"{hashtag}\n\nПрислал нечитаемое сообщение"
                    )
                break
    except Exception as e:
        print(f"Error copying message: {e}")
        print(f"Source chat: {message.chat.id}, Target chat: {chats_id.get(message.chat.id)}")

app.run()