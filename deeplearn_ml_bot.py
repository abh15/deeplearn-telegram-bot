#Requires python-telegram-bot,install using-
#pip python-telegram-bot
# Requires http://github.com/jetpacapp/DeepBeliefSDK



__author__ = 'MirSpur'

import telegram
import os
import urllib
import sys

def main():
    token = "your telegram bot token here"
    bot = telegram.Bot(token)  # Telegram Bot Authorization Token


    global LAST_UPDATE_ID
    LAST_UPDATE_ID = bot.getUpdates()[-1].update_id  # Get lastest update

    while True:
        for update in bot.getUpdates(offset=LAST_UPDATE_ID):
            text = update.message.text
            chat_id = update.message.chat.id
            update_id = update.update_id
            if LAST_UPDATE_ID < update_id:
                if text:
                    try:

                        urllib.urlretrieve(text, filename="foo.jpg")

                        os.system("sudo ./deepbelief foo.jpg > zcode.txt")
                        s1=os.popen("sort -k 2n zcode.txt | awk 'FNR==999 {$1=$2=\"\"; print}'").read()
                        s2=os.popen("sort -k 2n zcode.txt | awk 'FNR==998 {$1=$2=\"\"; print}'").read()
                        s3=os.popen("sort -k 2n zcode.txt | awk 'FNR==997 {$1=$2=\"\"; print}'").read()
			
			bot.sendMessage(chat_id=chat_id, text=s1+"\n"+s2+"\n"+s3)
                  	LAST_UPDATE_ID = update_id
                    except:
                #      	pass
			bot.sendMessage(chat_id=chat_id, text="Error:Cannot allocate GPU")
			sys.exit()


if __name__ == '__main__':
    main()
