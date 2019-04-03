import urllib.request 
import urllib.parse
from . import useragents

class BaiduSpider:
    def __init__(self):
        baseurl = 'http://www.baidu.com/f?'
        headers = random.choise(useragents.header_list)

    # 获取页面
    def get_page(self,url,headers): 
        req = request.Request(url,headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('urf-8')
        return req
    # 3. 保存数据
    def parse_page(self,filename):
        with open(filename, w) as f:

    # 4. zhu函数
    def url_page(self):
        name = input('请输入贴吧名')
        start = int(intpu('请输入起始页'))
        end = int(input('请输入终止页:'))
        for page in range(start,end+1):
            pn=[page-1]*50
            string=parse.urlencode({
                'kw':name,
                'pn':str(pn),
            })
            url =self.baseurl+string
            filename='%s-第%d页获取成功'%()
            html= self.get_page()