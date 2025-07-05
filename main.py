from telethon import TelegramClient, events
import re

from config import settings

api_id = settings.TELEGRAM_API_ID
api_hash = settings.TELEGRAM_API_HASH

# Hardcoded values, replace with your own
TARGETS_GROUPS = []
FORWARD_IDS = []
FORWARD_ALL = []
TARGET_WORDS = [ '.', 'вело', 'байк', 'велик', 'track', 'gt', 'thinkpad']


client = TelegramClient('my_account', api_id, api_hash)

def find_word_in_text(text, word):
    if not text:
        return False
    pattern = re.compile(re.escape(word), re.IGNORECASE)
    return bool(pattern.search(text))

@client.on(events.NewMessage(chats=TARGETS_GROUPS))
async def handler(event):
    text = event.raw_text
    for fw in FORWARD_ALL:
        try:
            await client.send_message(fw, text)
        except Exception as e:
            print(f"Error sending message to {fw}: {e}")
            continue
    for word in TARGET_WORDS:
        if find_word_in_text(text, word):
            for fw in FORWARD_IDS:
                print("Found", event)
                answer = f"Появилось новое объявление на тему {word}:\n date:{event.date}"
                try:
                    await client.send_message(fw, answer)
                    await client.forward_messages(fw, event.message)
                except Exception as e:
                    print(f"Error sending message to {fw}: {e}")

client.start()
client.run_until_disconnected()
