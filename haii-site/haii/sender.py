import asyncio
import json
from datetime import datetime

import aiocron
import redis
import requests
import telegram
from decouple import config

TOKEN_BOT_TELL = config('TOKEN_BOT_TELL')
ID_CHANNEL_TELL = config('ID_CHANNEL_TELL')
TOKEN_BOT_ETAA = config('TOKEN_BOT_ETAA')
ID_CHANNEL_EITAA = config('ID_CHANNEL_EITAA')

bot = telegram.Bot(token=TOKEN_BOT_TELL)

try:
    r = redis.StrictRedis(host="localhost", port=6379, db=0, password="", decode_responses=True)
except:
    print("[-] i can`t connect to redis!")


@aiocron.crontab('*/1 * * * *')
def clock():
    message = r.lrange('sender', 0, -1)
    message_json = list(map(lambda x: json.loads(x), message))
    result = list(filter(lambda x: x.get('postage_date') <= str(datetime.today()), message_json))
    for i in result:
        text = i.get('news')
        image = i.get('image', None)
        if image:
            with open(image, 'rb') as f:
                bot.sendPhoto(chat_id=ID_CHANNEL_TELL, photo=f, caption=text)
                requests.post(
                    f"https://eitaayar.ir/api/{TOKEN_BOT_ETAA}/sendFile",
                    data={
                        'chat_id': ID_CHANNEL_EITAA,
                        'caption': text,
                        'pin': int(0),
                    },
                    files={
                        'file': f,
                    }
                )
        else:
            bot.sendMessage(chat_id=ID_CHANNEL_TELL, text=text)
            requests.post(
                f"https://eitaayar.ir/api/{TOKEN_BOT_ETAA}/sendMessage",
                data={
                    'chat_id': ID_CHANNEL_EITAA,
                    'text': text,
                    'pin': int(0),
                },
            )
        r.lrem('sender', 1, json.dumps(i))


clock.start()
asyncio.get_event_loop().run_forever()
