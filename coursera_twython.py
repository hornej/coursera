import sys
from twython import Twython
from twython import TwythonStreamer

C_KEY = 'hf5yDnSSK4ey9mTU0JthTF6dD'
C_SECRET = 'gdhd5kueRljWdyoWL074j7Qa47dP26uez6Cx4zcNRDnGatmLbE'
A_TOKEN = '859823917870964736-k9D6DaLUqGFYP0kwnytwC5S9sDwj98P'
A_SECRET = 'gTz7aSnkMgK3wpzEgQb8x1xeSIJdO8d5ThPZh0n759Mcj'

api = Twython(C_KEY,C_SECRET,A_TOKEN,A_SECRET)

#api.update_status(status="hello world -RaspberryPi")

#search for text in streams
#statuses.filter()
#i.e. stream.statuses.filter(track = '')

##def blink():
##    GPIO.output(13,GPIO.HIGH)
##    time.sleep(1)
##    GPIO.output(13,GPIO,LOW)
found = 0

while True:
    class MyStreamer(TwythonStreamer):
        def on_success(self,data): #data is a dictionary passed on to on_success()
            if 'text' in data:
                found += 1
                print("Got it!",found)

    stream = MyStreamer(C_KEY,C_SECRET,A_TOKEN,A_SECRET)

    stream.statuses.filter(track="Ian G. Harris")

    if(found == 3):
        print("Ian G. Harris is popular!")

#execfile("...") will execute a python file inside python
