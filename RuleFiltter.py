#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tweepy

def isRule(tweet):
    #リプライのツイートなら
    if(tweet.in_reply_to_user_id is not None):
        return False

    #RTなら
    if(tweet.retweeted):
        return False

    #引用なら
    #if(tweet.quoted_status_id is not None):
    #    return False
    return True
