import re
from pyrogram import Client, filters

TARGETS_GROUPS = []
FORWARD_IDS = []
target_words = ['вело', 'байк', 'велик', 'track', 'gt', 'thinkpad']
def find_word_in_text(text, word):
    if not text:
        return False
    pattern = re.compile(re.escape(word), re.IGNORECASE)
    return bool(pattern.search(text))

app = Client("my_account")

@app.on_message(filters.chat(TARGETS_GROUPS))
async def search(client, message):
    text = message.text or message.caption
    for word in target_words:
        if find_word_in_text(text, word):
            for fw in FORWARD_IDS:
                print("Found", message)
                answer = f"Появилось новое объявление на тему {word}:\n date:{message.date}"
                await app.send_message(fw, answer)
                await message.forward(fw)
app.run()
