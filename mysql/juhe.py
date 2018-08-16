import urllib.request
import json
def juhe(gid):
    apiUrl = "http://web.juhe.cn:8080/finance/stock/hs"
    appKey = "e0caf324eb06620f0f7c890ca3711c66"


    apiUrl = "http://web.juhe.cn:8080/finance/stock/hs?gid=%s&key=%s"%(gid,appKey)
    request = urllib.request.Request(apiUrl)
    response = urllib.request.urlopen(request)
    res = response.read().decode('utf-8')
    res = json.loads(res)
    dapandata = {}
    if res['resultcode']=='200':
        dapandata = res['result'][0]['data']
    else:
        pass
    return dapandata