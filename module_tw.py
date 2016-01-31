"""
Module to emulate Rizon :tw functionality
"""
import json
import os
import base64
import logging

log = logging.getLogger('tw')

try:
    import requests, yaml  
    from requests_oauthlib import OAuth1
except ImportError as e:
    log.error("Error importing modules: %s" % e.strerror)

def _import_yaml_data(directory=os.curdir):
    try:
        settings_path = os.path.join(directory, "modules", "twitter.settings")
        return yaml.load(file(settings_path))
    except OSError:
            log.warning("Settings file for Twitter not set up; please create a Twitter API account and modify the example settings file.")
            return

def _get_twitter_auth():
    settings = _import_yaml_data()
    return OAuth1(settings['twitter']['consumer_key'],
            settings['twitter']['consumer_secret'])

def _handle_tweet(tweets):
    #reads dict
    ##You can modify the fields below or add any fields you want to the returned string
    try:
        id_num = tweets[0]['id']
        text = tweets[0]['text']
        user = tweets[0]['user']['screen_name']
        name = tweets[0]['user']['name']
        time = tweets[0]['created_at']
        tweet = "Most recent tweet by \x02%s\x02 (\x02@%s\x02) \x02\x0310|\x03\x02 %s \x02\x0310|\x03\x02 https://twitter.com/%s/status/%s \x02\x0310|\x03\x02 %s" % (name, user, text, user, id_num, time)
    except IndexError:
        tweet = "User not found."
    return tweet

def command_tws(bot, user, channel, args):
    """
    Performs a search on the twitter api, and returns the most relevant (as judged by Twitter) tweet.
    """

    pass

def command_tw(bot, user, channel, args):
    """
    Gets the most recent tweet tweeted by a twitter tweeter
    """
    tweet_url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={}"

    auth = _get_twitter_auth()
    twitapi = requests.get(tweet_url.format(args), auth=auth)

    ## load the content into a dict
    ## i do it the long way because sometimes requests.json() doesn't work (?)
    json1 = json.loads(twitapi.content.encode('utf-8'))
    tweet = _handle_tweet(json1)

    bot.say(channel, tweet.encode('utf-8'))
    return
