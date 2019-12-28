import urllib.request as urlrq
import urllib.parse
import json

strtotrans=input("请输入要翻译的句子:")
url="http://fanyi.youdao.com/translate"
data={}
data["i"]=strtotrans
data["from"]="AUTO"
data["to"]="AUTO"
data["smartresult"]="dict"
data["client"]="fanyideskweb"
data["salt"]="15505451847213"
data["sign"]="6d8ae1369d90f724fdd7ad574c70a847"
data["ts"]="1550545184721"
data["bv"]="8d165ec21fcdbdde58f225cd72fd33e4"
data["doctype"]="json"
data["version"]="2.1"
data["keyfrom"]="fanyi.web"
data["action"]="FY_BY_REALTIME"
data["typoResult"]="false"
data = urllib.parse.urlencode(data).encode("utf-8")
response= urlrq.urlopen(url,data)
html = response.read().decode("utf-8")
jsontrans=json.loads(html)
print("翻译的结果是:",jsontrans['translateResult'][0][0]["tgt"])