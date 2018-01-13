#! /usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup #HTML整形ツール
import requests

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

response   = session.get('https://twitter.com/',headers = headers, allow_redirects = True)
soup       = Beautifulsoup(response.text,"lxml")
auth_token = soup.find(attrs= {'name': 'authenticity_token'}).get('Value')

print("authenticity_token: "+auth_token)
