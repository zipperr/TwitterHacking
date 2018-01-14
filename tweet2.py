#! /usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
import requests
import sys

class TwitterTweet:
    def __init__(self):
        self.username = ""
        self.password = ""

    def tweet(self):
        session = requests.Session()

        headers = {
        "user-agent": "Mozilla/5.0",
        "accept":"text/html,application/xhtml+xml,application/xml;",
        "accept-language":"ja,en-US;q=0.8,en;q=0.6",
        "content-type":"application/x-www-form-urlencoded",
        "origin":"https://twitter.com",
        "referer":"https://twitter.com/",
        "upgrade-insecure-requests":"1"
        }
        payload = {
        "session[username_or_email]":"",
        "session[password]":"",
        "remember_me":"1",
        "return_to_ssl":"true",
        "scribe_log":"",
        "redirect_after_login":"/"
        }
        tweet = {
        "authenticity_token":"",
        "is_permalink_page":"false",
        "place_id":"",
        "status":"APIを使用していないツイート",
        "tagged_users":""
        }
        dest = {
        "authenticity_token":"",
        "is_permalink_page":"false",
        "place_id":"",
        "status":"APIを使用していないツイート",
        "tagged_users":""
        }
        try:
            response = session.get('https://twitter.com/',headers=headers,allow_redirects=False)
            soup = BeautifulSoup(response.text,"lxml")
            auth_token = soup.find(attrs={'name': 'authenticity_token'}).get('value')
        except ConnectionError:
            print ("[*]Twitterへ接続できません")
            sys.exit()

        payload["authenticity_token"] = auth_token
        tweet["authenticity_token"] = auth_token
        payload["session[username_or_email]"] = self.username
        payload["session[password]"] = self.password

        try:
            login = session.post('https://twitter.com/sessions',headers=headers,data=payload,allow_redirects=False)
            if login.status_code ==302:
                print ("[+] ログイン完了 HTTP ステータスコード:"),
                print (login.status_code)
            else:
                print("[+] ログイン失敗 HTTP ステータスコード:"),
                print(login.status_code)
        except:
            "[+]ログイン中に通信エラー"

        try:
            tweet = session.post("https://twitter.com/i/tweet/create",data=tweet,allow_redirects=False,headers=headers,cookies=login.cookies)
            if tweet.status_code ==200:
                print("[+]ツイート完了 HTTPステータスコード:")
                print(tweet.status_code)
            else:
                print("[+]ツイート失敗 HTTPステータスコード:")
                print(tweet.status_code)
        except:
            print("ツイート中にエラー")
if __name__ == "__main__":
    TwiTweet = TwitterTweet()
    TwiTweet.tweet()
