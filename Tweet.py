#!/usr/bin/env python
# -*- coding:utf-8 -*-


import tweepy
import AuthKey
import Timestamp
from pytz import timezone
from datetime import datetime
import RuleFiltter
import time

# 各種キーをセット
consumerKey =AuthKey.getConsumerKey()
collectAuth = tweepy.OAuthHandler(consumerKey["key"], consumerKey["secret"])

#読み込み専用アカウントの認証
collectKey = AuthKey.getCollectKey()
collectAuth.set_access_token(collectKey["token"], collectKey["secret"])

#書き込み専用アカウントの認証
tweetAuth = tweepy.OAuthHandler(consumerKey["key"], consumerKey["secret"])
tweetKey = AuthKey.getTweetKey()
tweetAuth.set_access_token(tweetKey["token"], tweetKey["secret"])



#APIインスタンスを作成
readApi = tweepy.API(collectAuth)
tweetApi = tweepy.API(tweetAuth)
oldDatetime=datetime.now(timezone('UTC'))

while True:
    print oldDatetime
    for tweet in readApi.user_timeline(readApi.me().id,count=10)[::-1]:
        if(timezone('UTC').localize(tweet.created_at) < oldDatetime):
            continue
        if(RuleFiltter.isRule(tweet) == False):
            continue
        print tweet.text
        tweetApi.update_status(status=tweet.text)

    oldDatetime= datetime.now(timezone('UTC'))
    time.sleep(30)
    print "hoge"

