#! /usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from requests.excecations import ConnectionError
from json import load
import socket, socks, requests
import random, sys, csv, time

class TwitterCreateAccount:
    def __init__(self):
        #串の設定
        ip = "localhost"
        port = 9050
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
        socket.socket = socks.socksocket
        self.screenname = "" #作成するユーザID
    def getScreenName(self):
        return self.screenname
    #Twitterに送信するメールアドレスの作成
    def mail(self):
        source_str      = "abcdefghijklmnopqrstuvwyz1234567890"
        username        = "unkoooo"   + "".join([random.choice(source_str) for x in xrange(8)])
        domain          = "unkoooo"   + "".join([random.choice(source_str) for x in xrange(8)])
        mail            = username + "@" + domain + ".com"
        self.screenname = username
        return mail
    def main(self):
        payload = {
        "authenticity_token":                   "",
        "signup_ui_metrics":                    '{"rf":{"febda18b516cb920a9677c97a37200bf06a75797203c67b3b77cf66bae703528":0,"e90cff83c8ac70e3fe5f93d3fdcfe81b1f16eefb6432341e2ca939888bffda81":-1,"d9fbce8a7838810d9655a09e1582dfb5544c77abf1e558def53a66897c9a60a0":1,"a33dd25f14f79eb9b8a5d86b7ae34fd3ab3b7645fd207771c16ad6e25cfb701b":1},"s":"cbBwVUAJJ_FCVdPszUrInfOMyM4B0Vzk03E4KNN1XvhO55ZhmdlyMGgQrLoZOdtNjL7fS6U5QZVJ_nUROQVazME6-Zbe7lL3MRwQqIm9gJN5AUEz9qJpmBnhHcY69Lxx5T6uz1s0PU2CqIcSVItHlXtf3BYZO7L2TBzjdIketanQktwPAM-SzVNqWCg1rCcPGmp2aSKPvMmLmaPOIeJFbRxyMcdllDZX6AWr7jYQcUY80GxqxadswOuqMXJuXGwhF_K_ZeRm2_LlcfgOH0unzu8M91T3C29ry5IloOmTGWxGC4RkUgbCS7sUgDKm2ro7BwOjy7x9r1x0oxNF815lRAAAAWD5jFl2"}',
        "m_metrics":                            "TxudD2kAkGwAIxtpD0QAomwA/xooD0oAsmwA4RoODycAw2wAyxr0DiIA1GwAvRrnDhMA5WwApxrnDhYA9WwAmBrnDg8ABW0AkRrnDgcAFm0AghrnDg8AJm0AdBraDhMAN20AZRraDg8ASG0AkwLaCwIYoXIIqQLaCxYAsnII3ALaCzMAvXIIjAPaC7AA13II3AMBDFkA3nIIfQR2DMcA7nIIJgXrDM0A/3IIlAVgDaAACXMI:Xh0WBXoB8QMAgx2UBx0AdBcAHBx/DiYRzDgA0x1/C3QDhU4A8wXnCAMYzVIAxBthEOETGmsAkwLaCwIYoXII",
        "d_metrics":                            "AABQRigjfgAAAABQRigjY0kCAABQRigjFrECAABQRigji3AIAABQRigj994J:AABQRigjY0kCAABQRigjFrECAABQRigji3AIAABQRigj994J",
        "user[name]":                           "",
        "user[email]":                          "",
        "user[user_password]":                  "passwd",
        "asked_cookie_personalization_setting": "1",
        "ad_ref":                               "",
        "user[discoverable_by_email]":          "1",
        "asked_discoverable_by_email":          "1",
        "user[discoverable_by_mobile_phone]":   "1",
        "asked_discoverable_by_mobile_phone":   "1"
        }
        tweet = {
        "authenticity_token": "",
        "is_permalink_page":  "false",
        "place_id":           "",
        "status":             "test",
        "tagged_users":       ""
        }
        follow = {
        "authenticity_token": "",
        "challenges_passed":  "false",
        "handles_challenges": "1",
        "user_id":            "1304509088"
        }
        fav = {
        "authenticity_token": "",
        "id":                 "952210691749892097",
        "tweet_stat_count":   "0"
        }
        retweet = {
        "authenticity_token": "",
        "id":                 "952210691749892097",
        "tweet_stat_count":   "0"
        }
        session = requests.Session()
        headers = {
        "User-Agent":"Mozilla/5.0",
        "accept":"test/html,application/xhtml+xml,application/xml;q=0.9, image/webp,*/*;q=0.8",
        "accept-language":"ja,en-US;q=0.8,en;q=0.6",
        "content-type":"application/x-www-form-urlencoded",
        "origin":"https://twitter.com",
        "referer":"https://twitter.com/",
        "upgrade-insecure-requests":"1"
        }
        try:
            response = session.get('https://twitter.com/',headers=headers,allow_redirects=False)
            soup = BeautifulSoup(response.text,"lxml")
            auth_token = soup.find(attrs={'name': 'authenticity_token'}).get('value')
        except ConnectionError:
            print ("[*]Twitterへ接続できません")
            sys.exit()

        #新規アカウントの生成処理
        try:
            try:
                payload['authenticity_token'] = auth_token
                payload['user[email]']        = self.mail()
                payload['user[name]']         = self.getScreenName()
                response = session.post('https://twitter.com/account/create', data=payload,  allow_redirects=False, headers=headers)
                print("[*]新規アカウント生成完了 HTTPステータスコード: ")
                print(response.status_code)
            except:
                print("[*]新規アカウントの生成に失敗しました")
            try:
                print("=====================================================================")
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
        except ConnectionError:
            print("[+] インターネットの接続が不安定のためプログラムを終了します")
            sys.exit()

    #ステータスコードの比較
        if response.status_code == 302:
            try:
                try:
                    response = session.get(url, headers=headers, allow_redirects=False)
                    print("[+] "+ url + "に接続 HTTPステータスコード: ")
                    print(response.status_code)
                except:
                    print("[+] "+ url + "に接続できません")

                if response.status_code != 200:
                    print("[+] このアカウントを使用するには携帯電話認証が必要です")
                    sys.exit()
                elif response.status_code == 200:
                    print("[+] 正常にアカウントが作成されました")
                    try:
                        follow["authenticity_token"]  = auth_token
                        tweet["authenticity_token"]   = auth_token
                        fav["authenticity_token"]     = auth_token
                        retweet["authenticity_token"] = auth_token

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
