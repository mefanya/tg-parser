from pyrogram import Client, filters
from settings import api_id, api_hash, session_name, chats_id

app = Client(session_name, api_id, api_hash)

@app.on_message(filters.all)
async def forward_message(client, message):
    try:
        chat_id = message.chat.id

        if hasattr(message, "message_thread_id") and message.message_thread_id:
            topic_id = message.message_thread_id
            print(f"Forum message detected: chat_id={chat_id}, topic_id={topic_id}")

            topic_name = None
            try:
                topics = await client.get_forum_topics(chat_id)
                for topic in topics.topics:
                    if topic.id == topic_id:
                        topic_name = topic.title
                        print(f"Found topic name: {topic_name}")
                        break
            except Exception as e:
                print(f"Error fetching forum topics: {e}")

            if topic_name:
                key = (chat_id, topic_name) 
                if key in chats_id:
                    target_chat_id = chats_id[key]
                    print(f"Forwarding message from topic '{topic_name}' to chat {target_chat_id}")
                    await client.forward_messages(target_chat_id, chat_id, message.id)

        else:
            if chat_id in chats_id:
                target_chat_id = chats_id[chat_id]
                print(f"Forwarding message from chat {chat_id} to chat {target_chat_id}")
                await client.forward_messages(target_chat_id, chat_id, message.id)

    except Exception as e:
        print(f"Error forwarding message: {e}")

app.run()