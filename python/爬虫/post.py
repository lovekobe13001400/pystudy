#coding=utf-8
import urllib.request
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
headers={"User-Agent": "Mozilla...."}
formdata = {
    "type":"AUTO",
    "i":"i love python",
    "doctype":"json",
    "xmlVersion":"1.8",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_ENTER",
    "typoResult":"true"
}

data = urllib.parse.urlencode(formdata).encode(encoding='utf-8')
request = urllib.request.Request(url,data,headers=headers)
response = urllib.request.urlopen(request)
page = response.read().decode('utf-8');
fo = open("test.txt", "w",encoding='utf-8')
fo.write(page)

