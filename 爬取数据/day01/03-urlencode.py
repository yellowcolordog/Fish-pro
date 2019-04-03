import urllib.request
import urllib.parse

# 定义常用变量
baseurl = "http://www.baidu.com/?"
headers = {
    'User-Agent':'',

}
key = input('请输入需要搜索的内容:\n')

# 编码, 拼接URL地址
wd = urllib.parse.urlencode({'wd':key})
url = baseurl + wd 

# 发请求, 获响应
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
html = response.read().decode()

with open('/home/tarena/正式课/爬虫/day01/1.txt','w') as fw:   
    fw.write(html)