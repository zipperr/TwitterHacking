#! /usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from requests.excecations import ConnectionError
from json import load
import socket, socks, requests, random, sys, csv, time

class TwitterCreateAccount:
	def __init__(self):
		#串の設定
		ip = 'localhost' #自分の使用するプロキシのIPアドレス
		port = 9050 #自分の使用するプロキシのポート番号
		socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
		socket.socket = socks.socksocket
		self.screenname = "" #作成するユーザ名


	def getScreenName(self):
		return self.screenname

	#Twitterに送信するメールアドレスの作成
	def mail(self):
		source_str      = 'abcdefghijklmnopqrstuvwyz1234567890'
		username        = "r00t"   + "".join([random.choice(source_str) for x in xrange(8)])
		domain          = "r00t"   + "".join([random.choice(source_str) for x in xrange(8)])
		mail            = username + "@" + domain + ".com"
		self.screenname = username
		return mail

	def main(self):
		#新規アカウント作成POST送信のリクエスト
		payload = {
			"authenticity_token":                   "",
			"signup_ui_metrics":                    '{"rf":{""}',
			"user[name]":                           "",
			"user[email]":                          "",
			"user[user_password]":                  "新規アカウントのパスワード",
			"asked_cookie_personalization_setting": "1",
			"ad_ref":                               "",
			"user[discoverable_by_email]":          "1",
			"asked_discoverable_by_email":          "1",
			"user[discoverable_by_mobile_phone]":   "1",
			"asked_discoverable_by_mobile_phone":   "1"
		}

		#ツイートPOSTの送信リクエスト
		tweet ={
			"authenticity_token": "",
			"is_permalink_page":  "false",
			"place_id":           "",
			"status":             "#zippeer Hello",
			"tagged_users":       ""
		}

		#フォローPOSTの送信リクエスト
		tweet ={
			"authenticity_token": "",
			"challenges_passed":  "false",
			"handles_challenges": "1",
			"user_id":            "ユーザーID??????????"
		}
		#お気に入りPOST送信リクエスト
		fav ={
			"authenticity_token": "",
			"id":                 "ID?????????????????????",
			"tweet_stat_count":   "0"
		}

		#リツイートPOST送信リクエスト
		retweet = {
			"authenticity_token": "",
			"id":                 "ID?????????????????????",
			"tweet_stat_count":   "0"
			}

		#セッション生成
		session = requests.Session()

		#Twitterへ送信するヘッダー情報
		headers ={
			"User-Agent":                "Mozilla/5.0",
			"accept":                    "test/html,application/xhtml+xml,application/xml;q=0.9, image/webp,*/*;q=0.8",
			"accept-language":           "ja,en-US;q=0.8,en;q=0.6",
			"content-type":              "application/x-www-form-urlencoded",
			"origin":                    "https://twitter.com",
			"referer":                   "https://twitter.com/",
			"upgrade-insecure-requests": "1"
		}

# authenticity_token値の取得
try:
	response   = session.get('https://twitter.com/',headers = headers, allow_redirects = False)
	soup       = Beautifulsoup(response.text,"lxml")
	auth_token = soup.find(attrs= {'name': 'authenticity_token'}).get('value')
except ConnectionError:
	print("[*]Twitterへ接続できません")
	sys.exit() 

#新規アカウントの生成処理
try:
	try:
		#送信リクエスト内容のセット
		payload['authenticity_token'] = auth_token
		payload['user[email]']        = self.mail()
		payload['user[name]']         = self.getScreenName()
		#アカウント生成リクエスト送信
		response = session.post('https://twitter.com/account/create', data=payload,  allow_redirects=False, headers=headers)
		print("[*]新規アカウント生成完了 HTTPステータスコード: ")
		print(response.status_code)
	except:
		print("[*]新規アカウントの生成に失敗しました")
	try:
		#POST送信後に送信データの表示
		print("=====================================================================")
		#各変数に表示文字列挿入
		twitter_username =payload['user[name]']
		url = "https://twitter.com/" + payload['user[name]']
		print("[+] authenticityトークン..................:" + payload['authenticity_token'])
		print("[+] タイムラインURL.......................:" + url )
		print("[+] ユーザ名..............................:" + payload['user[name]'])
		print("[+] アカウントメールアドレス..............:" + payload['user[email]'])
		print("[+] アカウントパスワード..................:" + payload['user[user_password]'])
		print("=====================================================================")
	except:
		print("[+] 作成に成功しましたが、成功結果の表示中にエラーが発生しました")
	print("[+] インターネットの接続が不安定のためプログラムを終了します")
	sys.exit()

	#ステータスコードの比較
	if response.status_code == 302:
		try:
			try:
				#url変数にはhttps://twitter.com/生成したアカウントID値が入っている
				response = session.get(url, headers=headers, allow_redirects=False)
				print("[+] "+ url + "に接続 HTTPステータスコード: ")
				print(response.status_code)
			except:
				print("[+] "+ url + "に接続できません")
			#アカウント名で作成されているか確認
			if response.status_code != 200:
				print("[+] このアカウントを使用するには携帯電話認証が必要です")
				sys.exit()
			elif response.status_code == 200:
				print("[+] 正常にアカウントが作成されました")
				#任意の処理(フォロー・ツイート・お気に入り・リツイート)
				try:
					follow['authenticity_token']  = auth_token
					tweet['authenticity_token']   = auth_token
					fav['authenticity_token']     = auth_token
					retweet['authenticity_token'] = auth_token

					response = session.post('https://twitter.com/i/user/follow', data=follow, allow_redirects=False, headers=headers, cookies=response.cookies)
					print("[+] フォロー完了 HTTPステータスコード :")
					print(response.status_code)

					response = session.post('https://twitter.com/i/tweet/create', data=tweet, allow_redirects=False, headers=headers, cookies=response.cookies)
					print("[+] ツイート完了 HTTPステータスコード :")
					print(response.status_code)

					response = session.post('https://twitter.com/i/tweet/like', data=fav, allow_redirects=False, headers=headers, cookies=response.cookies)
					print("[+] お気に入り完了 HTTPステータスコード :")
					print(response.status_code)

					response = session.post('https://twitter.com/i/tweet/retweet', data=retweet, allow_redirects=False, headers=headers, cookies=response.cookies)
					print("[+] リツイート完了 HTTPステータスコード :")
					print(response.status_code)

				except:
					print("[+] フォロー失敗")
				finally:
					sys.exit()
		except ConnectionError:
				print("[+] "+ url +"接続エラー")
				sys.exit()
		finally:
				return
	else:
			#デバッグのための表示
			print("[+] HTTPステータスコード :")
			print(response.status_code)

	if __name__ == '__main__':
		TwiACC       = TwitterCreateAccount()
		start        = time.time()
		TwiACC.main()
		elapsed_time = time.time() - start
		print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
