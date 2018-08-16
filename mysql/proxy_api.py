#六六代理动态ip
import urllib.request
def proxy_list():
    url = "http://api.66daili.cn/API/GetSecretProxy/?orderid=1740736031801110440&num=20&token=66daili&format=text&line_separator=win&protocol=http&region=domestic"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    res = response.read().decode('utf-8')
    res = res.split('\r\n')
    return res