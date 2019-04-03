import urllib.request

url = 'http://www.baidu.com'
header={
    "User-Agent":'Mozilla/5.0',

}
# 1 创建请求对象
request = urllib.request.Request(url,headers=header)
# 2 获取响应对象
response = urllib.request.urlopen(request)
# 3 获取内容
html = response.read().decode()

print(response.getcode())