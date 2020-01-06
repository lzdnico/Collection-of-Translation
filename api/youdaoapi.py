# -*- coding: utf-8 -*-
import sys
import uuid
import requests
import hashlib
import time
import json
import urllib
import api.apikey
YOUDAO_URL = 'https://openapi.youdao.com/api'
APP_KEY = api.apikey.youdaoAPP_KEY                                  
APP_SECRET = api.apikey.youdaoAPP_SECRET                


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def connect(q):
    data = {}
    data['from'] = 'auto'
    data['to'] = 'en'
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign
    response = do_request(data)
    ans = str(json.loads(response.text)["translation"])
    ans = ans.replace('[\'','').replace('\']','').replace('\\n','\n')
    return ans


#connect('有道翻译测试。\n电力电子得到快速发展')