
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, re, smtplib, time, twilio, datetime
from email.mime.text import MIMEText

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'eVo5jtQTuGPNr9Cujj8kuh2BD'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'pLbS9TnhP4n8pq12Q1pn1YYbEaUpUsdAs8yQ4T2AQCBZUmhukB'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '3232201825-07tHHHQ648U0S8cFHaaCZZumDAJHvLU3KvhlKbE'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'lsodWGLRa3ApngRClBFos8pcq3NH9TPPJSpTFJOXXu65u'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for i in range(1000000):
    for tweet in api.user_timeline("NikkiBenderXXX"):
        tweetDate = tweet.created_at.replace(hour=0, minute=0, second=0, microsecond=0)
        if datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) == tweetDate:
            if re.search("[on]+\slive", tweet.text):
                print tweet.created_at
                msgSent = True
                from twilio.rest import TwilioRestClient
                accountSid = "AC47085ae94f517bc6aef0a6fa0cd5d7c0"
                authToken = "76fbe4b924b7954ecbe90dd19697d324"
                twilioClient = TwilioRestClient(accountSid, authToken)
                myTwilioNumber = "1702-534-4456"
                destCellPhone = "+918883340453"
                myMessage = twilioClient.messages.create(body = "live", from_=myTwilioNumber, to=destCellPhone)
    if msgSent == True:
        break
    time.sleep(600)
