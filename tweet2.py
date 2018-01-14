#! /usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
import requests, sys

class TwitterTweet:
	def __init__(self):
		#ログインするユーザ名
		self.username = "xxxxxx"
		#ログインユーザのパスワード
		self.password = "xxxxxx"

	def tweet(self):
		try:
			#セッション生成
			session = requests.Session()
			headers ={
				"User-Agent":                "Mozilla/5.0",
				"accept":                    "test/html,application/xhtml+xml,application/xml;",
				"accept-language":           "ja,en-US;q=0.8,en;q=0.6",
				"content-type":              "application/x-www-form-urlencoded",
				"origin":                    "https://twitter.com",
				"referer":                   "https://twitter.com/",
				"upgrade-insecure-requests": "1"
			}

			#twitterログインに必要な引数
			payload={
				"session[username_or_email]": "", 
				"session[password]": "", 
				"remember_me": "1", 
				"retune_to_ssl": "true", 
				"scribe_log": "", 
				"redirect_after_login": "/", 
			}

			# ツイートPOST送信のリクエスト
			tweet ={
				"authenticity_token": "",
				"is_permalink_page": "false",
				"place_id": "",
				"status": "test",
				"tagged_users": "",
			}

		# authenticity_token値の取得
			response = session.get('https://twitter.com/',headers = headers, allow_redirects = False)
			soup       = BeautifulSoup(response.text,"lxml")
			auth_token = soup.find(attrs= {'name': 'authenticity_token'}).get('value')
		except ConnectionError:
			print("[*]Twitterへ接続できません")
			sys.exit() 
		
			#authenticity_tokenをpayloadに設定
			payload['authenticity_token'] = auth_token
			#authenticity_tokenをツイートに設定
			tweet['authenticity_token']=auth_token
			#ユーザーIDをpayloadに設定
			payload['session[username_or_email]'] = self.username
			#パスワードをpayloadに設定
			payload['session[password]'] = self.password
		#twitterにログイン
		try:
			login =session.post('https://twitter.com/sessions', headers=headers, data=payload, allow_redirects=False)
			if login.status_code == 302:
				print("[+] ログイン完了 HTTPステータスコード: ")
				print(login.status_code)
			else:
				print("[+] ログイン失敗 HTTPステータスコード: ")
				print(login.status_code)
		except:
			print("[+] ログイン中に通信エラー")
		#ツイートを投稿
		try:
			tweet = session.post('https://twitter.com/i/tweet/create', data=tweet, allow_redirects=False, headers=headers, cookies=login.cookies)
			if tweet.status_code == 200:
				print("[+] ツイート完了 HTTPステータスコード: ")
				print(tweet.status_code)
			elif tweet.status_code == 403:
				response = session.get('https://twitter.com/アカウント名', headers=headers, allow_redirects=False)
				soup       = Beautifulsoup(response.text,"lxml")
				destroy['id'] = soup.find('div', attrs={'class':'stream-container'}).get('data-max-position')
				dest = session.post('https://twitter.com/i/tweet/destroy', allow_redirects=False,headers=headers, cookies=login.coo)
				if dest.status_code == 200:
					print("[+] 重複ツイート削除成功 HTTPステータスコード: ")
					print(dest.status_code)
				else:
					print("[+] 重複ツイート削除失敗 HTTPステータスコード: ")
					print(dest.status_code)
		except:
			print("[+] ツイート中に通信エラー")

if __name__ == '__main__':
	TwiTweet = TwitterTweet()
	TwiTweet.tweet()
