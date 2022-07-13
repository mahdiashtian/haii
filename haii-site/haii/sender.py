import redis
import asyncio
import aiocron
import json
from settings import MEDIA_ROOT
from decouple import config
from datetime import datetime
import requests
import telegram
import os

TOKEN_BOT_TELL = config('TOKEN_BOT_TELL')
ID_CHANNEL_TELL = config('ID_CHANNEL_TELL')
TOKEN_EITAA_BOT = config('TOKEN_EITAA_BOT')

bot = telegram.Bot(token=TOKEN_BOT_TELL)


try:
    r = redis.StrictRedis(host="localhost", port=6379, db=0, password="", decode_responses=True)
except:
    print("[-] i can`t connect to redis!")


@aiocron.crontab('*/1 * * * *')
def clock():
    message = r.lrange('sender', 0, -1)
    message_json = list(map(lambda x: json.loads(x),message))
    result = list(filter(lambda x:x.get('date_of_send')<=str(datetime.today()),message_json))
    for i in result:
        text = i.get('news')
        image = i.get('image',None)
        if image:
            with open(image,'rb') as f:
                bot.sendPhoto(chat_id=ID_CHANNEL_TELL,photo=f,caption=text)
                requests.post(
                    f"https://eitaayar.ir/api/{TOKEN_EITAA_BOT}/sendFile",
                    data={
                        'chat_id': '8168633',
                        'caption': text,
                        'pin': int(0),
                    },
                    files={
                        'file': f,
                    }
                )
        else:
            requests.post(
                f"https://eitaayar.ir/api/{TOKEN_EITAA_BOT}/sendMessage",
                        data={
                            'chat_id': '8168633',
                            'text': text,
                            'pin': int(0),
                        },
            )
            bot.sendMessage(chat_id=ID_CHANNEL_TELL,text=text)
        r.lrem('sender',1,json.dumps(i))
clock.start()
asyncio.get_event_loop().run_forever()
