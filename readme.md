# Telegram Notification Bot

This Python script, built with the [Telethon](https://docs.telethon.dev/) library, monitors specific Telegram chats for messages containing certain keywords and forwards them to designated chats or users.

## How to Get API ID and Hash

1. Go to https://my.telegram.org/
2. Log in with your Telegram account.
3. Create a new application to get your `api_id` and `api_hash`.
4. Add these credentials to your `config.py` or environment as required by the script.

## Main Features

- **Keyword Detection**: The script checks messages in `TARGETS_GROUPS` for keywords such as 'bike', 'track', 'gt', 'thinkpad', and others.
- **Message Forwarding**: If a message contains any of the keywords, it is forwarded to all chats listed in `FORWARD_IDS`.
- **Forward All**: All messages from monitored groups can be forwarded to chats listed in `FORWARD_ALL`.
- **Flexible Configuration**: You can easily change the monitored groups, keywords, and forwarding targets in the script.

<!-- ## How to Get Chat or User ID

- You can use [@userinfobot](https://t.me/userinfobot) in Telegram to get your user or group ID.
- Or use a simple Telethon script:
  ```python
  from telethon import TelegramClient
  api_id = 'YOUR_API_ID'
  api_hash = 'YOUR_API_HASH'
  async def main():
      async with TelegramClient('anon', api_id, api_hash) as client:
          entity = await client.get_entity('username_or_channel')
          print(entity.id)
  import asyncio; asyncio.run(main())
  ``` -->

## Notes

- For supergroups and channels, IDs usually start with `-100`.
- You must have previously interacted with users/chats to send them messages via Telethon.
- If you get `ValueError: Could not find the input entity`, make sure you have written to the user or joined the group/channel.