#百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json
import api.apikey

appid = api.apikey.baiduappid  
secretKey = api.apikey.baidusecretKey 

httpClient = None
fromLang = 'auto'   #原文语种
toLang = 'en'   #译文语种

def baidu(q):
    try:
        salt = random.randint(32768, 65536)
        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = '/api/trans/vip/translate'
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign    
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        if httpClient:
            httpClient.close()
        ans = ''
        for dst in result['trans_result']:
            ans += '\n'+dst['dst']
        #print(ans)
        return (ans)

    except Exception as e:
        return (e)
#baidu('电力电子技术得到广泛的应用。\n原来越多的设备得到使用。')