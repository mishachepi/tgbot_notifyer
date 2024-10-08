# Tg bot for notification

This Python script, built with the [Pyrogram](https://docs.pyrogram.org/) library, monitors specific Telegram chats for messages containing certain keywords and forwards them to designated chats.

## Main Features

- **Keyword Detection**: The script checks messages in `TARGETS_GROUPS` for keywords like 'bike', 'track', 'gt', and 'thinkpad'.
- **Message Forwarding**: If a message contains any of the keywords, it's forwarded to chats listed in `FORWARD_IDS`.

## Usage

1. Set `TARGETS_GROUPS` to the chats to monitor.
2. Add forwarding chat IDs to `FORWARD_IDS`.
3. Run the script. It will search for keywords and forward relevant messages.
