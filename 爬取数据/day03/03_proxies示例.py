import requests
from random import choice

# 测试网址, 能显示出口IP
useragents = [
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'},
    {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50'},
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12'},
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201'},
    {'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0"},
]

url = 'http://www.ip138.com/'
headers=choice(useragents)
proxies = {
    'http':'http://309435365:szayclhp@116.255.191.105:16816',
    # 'https':'https://309435365:szayclhp@116.255.191.105:16816',
    # 'http':'http://121.61.0.79:9999',
    }

res = requests.get(url,headers= headers,
proxies=proxies,timeout=2)
res.encoding='gb2312'
print(res.text)

# 163.204.241.154 	9999 	广东 	高匿 	HTTPS 	 1分钟 	19-03-21 22:00
# 116.209.54.83 	9999 	湖北仙桃 	高匿 	HTTP 	 1分钟 	19-03-21 21:21
# 27.29.44.220 	9999 	湖北 	高匿 	HTTP 	 77天 	19-03-21 20:21
# 183.148.153.147 	9999 	浙江台州 	高匿 	HTTP 	 1分钟 	19-03-21 20:21