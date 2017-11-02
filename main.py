import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import telegram

#twitter
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

#telegram
bot = telegram.Bot('token')


class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        Manejor.convert(data)
        return True

    def on_error(self, status):
        print(status)


class Manejor:
    def convert(data):
        jso = json.loads(data)
        try:
            user = jso['user']['screen_name']
            text = jso['text']
            #id de a quien se va a enviar el telegram
            bot.send_message(chat_id='', text="@" + user + "\n" + text)

        except:
            print("Error")


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    #lo que se va a seguir en twitter
    stream.filter(track=['#twitter'])
