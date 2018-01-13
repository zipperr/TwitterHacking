#! /usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup #HTML整形ツール
from requests.excecations import ConnectionError
import requests, sys

class TwitterLogin:
	def __init__(self):
		#ログインするユーザ名
		self.username = "アカウントめい"
		#ログインユーザのパスワード
		self.password = "パスワード"

def login(self):

		#セッション生成
		session = requests.Session()
		headers ={
			"User-Agent":                "Mozilla/5.0",
			"accept":                    "test/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
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

# authenticity_token値の取得
	try:
		response   = session.get('https://twitter.com/',headers = headers, allow_redirects = False)
		soup       = Beautifulsoup(response.text,"lxml")
		auth_token = soup.find(attrs= {'name': 'authenticity_token'}).get('Value')
	except ConnectionError:
		print("[*]Twitterへ接続できません")
		sys.exit() 

	#authenticity_tokenをpayloadに設定
	payload['authenticity_token'] = auth_token
	#ユーザーIDをpayloadに設定
	payload['session[username_or_email]'] = self.username
	#パスワードをpayloadに設定
	payload['session[password]'] = self.password

	#twitterにログイン
	try:
		login =session.post('https://twitter.com/session', headers=headers, data=payload, allow_redirects=False)
		if login.status_code == 302:
			print("[+] ログイン完了 HTTPステータスコード: ")
			print(login.status_code)
		except:
			print("[+] ログイン中に通信エラー")

if __name__ == '__main__':
	TwiLogin = Twitterlogin()
	TwiLogin.login()
