#实例 模拟翻译


import urllib.request
import urllib.parse
import json

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
data = {}
data['type'] = 'AUTO'
data['i'] = 'i love you'
data['doctype'] = 'json'
data['xmlVersion'] = '1.6'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['typoResult'] = 'false'
data['action'] = 'FY_BY_CLICKBUTTION'
data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url, data)
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.3')
response = urllib.request.urlopen(req)


html = response.read().decode('utf-8')

print(html)


target = json.load(html)


