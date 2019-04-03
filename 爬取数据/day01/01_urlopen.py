"""向百度发起请求, 并获取响应内容"""
from urllib.request import urlopen

url = 'http://www.baidu.com/'
response = urlopen(url)
print(dir(response))
# print(response)
print(response.read().decode('utf-8'))