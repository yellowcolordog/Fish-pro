from urllib import request
from urllib import request
import random

# 定义常用变量
baseurl = "http://tieba.baidu.com/f?"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    'User-Agent2':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'
}

# 接收用户输入, 拼接URL地址, 发请求
name = input('请输入贴吧名')
start = int(intpu('请输入起始页'))
end = int(input('请输入终止页:'))
# for 循环拼接URL地址, 发请求
for page in range(start,end+1):
    pn = (page-1)*50
    string = parse.urlencode({'wb':name,'pn':str(pn)})
    url = baseurl+string
    # 发请求
    headers = random.choise(headers_list)
    req = request.Request(url,headers=headers)
    res = request.urlopen(req)
    html = res.read().decode()
    # 写入本地文件
    filename="{}"
    with open(filename,'w'),as f:
        r.write(html)
        print('第%d页爬去税金')甜蜜拍人 