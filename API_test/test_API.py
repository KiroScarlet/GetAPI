#!/usr/bin/env python3
# -*- coding: gbk -*-
import urllib.request, sys
import ssl


host = 'https://jisuznwd.market.alicloudapi.com'
path = '/iqa/query'
method = 'GET'
appcode = '17d9e7ec04e34d179bdad0fca0518220'
querys = 'question=%E6%9D%AD%E5%B7%9E%E5%A4%A9%E6%B0%94'
bodys = {}
url = host + path + '?' + querys

request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib.request.urlopen(request, context=ctx)
content = response.read()
if (content):
    print(content)