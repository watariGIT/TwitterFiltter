#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tweepy
import AuthKey

consumerKey =AuthKey.getConsumerKey()
tweetAuth  = tweepy.OAuthHandler(consumerKey["key"], consumerKey["secret"])
redirect_url = tweetAuth.get_authorization_url()
print 'Get your verification code from: ' + redirect_url
verifier = raw_input('Type the verification code: ').strip()
tweetAuth.get_access_token(verifier)
print 'ACCESS_TOKEN: '+ tweetAuth.access_token
print 'ACCESS_SECRET: ' + tweetAuth.access_token_secret

