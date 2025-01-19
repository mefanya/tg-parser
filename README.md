# README

## Telegram Bot for Forwarding Messages

This bot is built using the [Pyrogram](https://docs.pyrogram.org/) library. It forwards messages from specific source chats to target chats, as defined in a dictionary.

## Features

- **Chat ID Retrieval**: Use the `.type` command to get the chat ID of any chat.
- **Message Forwarding**: Automatically forwards messages from source chats to target chats as specified in the configuration.

## Prerequisites

- Python 3.0 or higher
- `pyrogram` library installed
- A Telegram API ID and API Hash

## Installation

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. Install Dependencies

This project uses [Poetry](https://python-poetry.org/) for dependency management. To install dependencies, run:

```bash
poetry install
```

### 3. Set Up Configuration

Create a `config.ini` file in the project folder with the following content:

```ini
[pyrogram]
api_id = your_api_id
api_hash = your_api_hash
```

Create a `settings.py` file in the project folder with the following content:

```python
session_name = "<your_session_name>"

chats_id = {
    -1001234567890: -1009876543210,  # Replace with your source_chat: target_chat pairs
    -1001122334455: -1005544332211,
}
```

Replace the placeholders with your actual values:

- `api_id` and `api_hash` from [Telegram's my.telegram.org](https://my.telegram.org/).
- `session_name` can be any string.
- `chats_id` is a dictionary where keys are source chat IDs and values are target chat IDs.

### 4. Run the Bot

To run the bot, use Poetry:

```bash
poetry run python main.py
```

## Usage

### Retrieve Chat ID

1. Go to a chat in Telegram where the bot is a member.
2. Send the command `.type`.
3. Check the console output for the chat ID.

### Forward Messages

1. Ensure the bot is a member of all source and target chats defined in `chats_id`.
2. The bot will automatically forward messages from source chats to target chats when it receives them.

## Error Handling

If any issues occur during message forwarding, the bot will log the error in the console with a message like:

```text
Error: <error_message>
```

## Example

**config.ini** example:

```ini
[pyrogram]
api_id = 123456
api_hash = abcd1234efgh5678ijkl
```

**settings.py** example:

```python
session_name = "my_bot_session"

chats_id = {
    -1001111111111: -1002222222222,  # Forward from Chat A to Chat B
    -1003333333333: -1004444444444,  # Forward from Chat C to Chat D
}
```

## Notes

- The bot requires access to both source and target chats. Make sure the bot has sufficient permissions to read messages in source chats and send messages in target chats.
- Use a secure method to store your `api_id` and `api_hash`. Avoid hardcoding sensitive information directly in the script if possible.
