##############################################################################################################################################################################################################################################

#Import packages
##############################################################################################################################################################################################################################################
import tweepy as tp 
import re
import time
import logging
from os import environ
from requests_html import HTMLSession
from os import environ
from keys import CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import json


##############################################################################################################################################################################################################################################
#access account
##############################################################################################################################################################################################################################################
auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tp.API(auth)



##############################################################################################################################################################################################################################################
# script
##############################################################################################################################################################################################################################################

def parse_input():
    mentions = api.mentions_timeline()
    replies = api.user_timeline()
    att = replies[0]._json
    user = mentions[0]._json
    if not att['in_reply_to_status_id'] == user['id']:
        full_comment = re.split("\s", mentions[0].text)
        for i, j in enumerate(full_comment):
            if "@BotHadith" == j:
                author = full_comment[i+1]
                book = full_comment[i+2]
                hadith = full_comment[i+3]
            else:
                pass
        return author, book, hadith, mentions

                
def hadith_call(author, book, hadith):
    base= "https://sunnah.com/"
    url = base + '/' + author + '/' + str(book) + '/' + str(hadith)
    session = HTMLSession()
    r = session.get(url)
    s = r.html.find('.english_hadith_full', first=True)
    post = s.text
    link = "Link to the Hadith: %s" % (url)
    return post, link

def post_hadith_tweet(post, url, mentions):
    thread = str(post) + '  ' + str(url)
    if len(thread) < 200:
        api.update_status('@' + mentions[0].user.screen_name + '  ' + thread)
    else:
        try:
            n = 200
            for i in range(0, len(thread), n):
                api.update_status('@' + mentions[0].user.screen_name + '  ' + thread[i:i+n], in_reply_to_status_id = mentions[0].id ,auto_populate_reply_metadata=True) 
        except:
            pass


##############################################################################################################################################################################################################################################
#run script
##############################################################################################################################################################################################################################################

if __name__ == "__main__":
    # while True:
    #     author, book, hadith, mentions = parse_input()
    #     post, link = hadith_call(author,book,hadith)
    #     post_hadith_tweet(post, link, mentions)
    #     time.sleep(30)

