from telethon import TelegramClient
from config import settings

api_id = settings.TELEGRAM_API_ID
api_hash = settings.TELEGRAM_API_HASH

chats = ['group_name', 'group_name2'] # https://t.me/THIS_IS_GROUP_NAME

async def main():
    async with TelegramClient('anon', api_id, api_hash) as client:
        for chat_username in chats:
            entity = await client.get_entity(chat_username)
            print(f"ID чата @{chat_username}: {entity.id}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())