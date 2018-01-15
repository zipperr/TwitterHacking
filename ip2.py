#! /usr/bin/env python
# -*- coding: utf-8 -*-
import socket, socks, requests
import requests

class Tor:
	def  __init__(self):
		#串の設定
		ip = "localhost" #自分の使用するプロキシのIPアドレス
		port = 9050 #自分の使用するプロキシのポート番号
		socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
		socket.socket = socks.socksocket

	def get_ip(self):
		#セッション生成
		session = requests.Session()
		try:
			ip_addr = session.get("https://api.ipify.org/").text
			return ip_addr
		except socks.ProxyConnectionError:
			print("[+]Proxy Error")
		return

if __name__ == "__main__":
	Tor =Tor()
	ip = Tor.get_ip()
	print(ip) #Tor経由のIPアドレス表示
