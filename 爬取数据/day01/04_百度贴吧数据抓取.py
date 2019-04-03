from urllib import request
from urllib import parse
import random
import time

# 定义常用变量
baseurl = 'http://tieba.baidu.com/f?'
header_list = [
  {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'},
  {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'},
  {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER'}
]
# 接收用户输入,拼接URL地址,发请求
name = input('请输入贴吧名称:')
start = int(input('请输入起始页:'))
end = int(input('请输入终止页:'))
# for循环拼接URL地址,发请求
for page in range(start,end+1):
  pn = (page-1)*50
  # string : 'kw=%E8...&pn=...'
  string = parse.urlencode(
                    {'kw':name,'pn':str(pn)})
  url = baseurl + string
  # 发请求
  headers = random.choice(header_list)
  req = request.Request(url,headers=headers)
  res = request.urlopen(req)
  html = res.read().decode('utf-8')
  # 写入本地文件
  filename = '%s-第%d页.html' % (name,page)
  with open(filename,'w') as f:
    f.write(html)

  print('第%d页爬取成功' % page)
  time.sleep(1)










