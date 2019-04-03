2. csv模块  
  import csv 
  with open('test.csv','a',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerrow([])

3. MySQL数据库
  import pymysql 
  db = pymysql.connect('localhost','root','123456',charset='utf8')
  cursor = db.cursor()
  cursor.execute('sql命令',[%s的参数])

4. MongoDB流程
  import pymongo
  1. conn = pymongo.MongoClient('ip地址',27017)
  2. db = conn['库名']
  3. myset = db['集合名']
  4. myset.insert_one(D)

5. requests.get(url,headers=headers)
   向网站发起请求并获取响应对象
   1. 响应对象(res)属性
   ...

**********************************************
Day03笔记
1. 腾讯招聘作业

2. requests.get()方法参数
  1. 查询参数(params): 字典
    res = requests.get(url,params=params,headers=headers)
    * 自动对params字典编码, 然后和url拼接, 发请求
    示例: 输入百度搜索内容, 爬取第2页数据
  keywords=...&start=...
  2. 代理参数(proxies): 字典
    1. 获取代理IP的网站
      西刺代理
      块代理
      高匿: 看不到用户ip, 只能看到代理ip
    2. 普通代理
      1. 格式: proxies={'协议':'协议://IP:PORT'}
      2. 测试网站
        http://httpbin.org/get
        https://whatismyip.com
    3. 私密代理
      1. 格式
        proxies={'协议':'协议://用户名:密码@IP:端口'}
  3. web客户端验证(auth): 元组
    1. auth=('用户名','密码')
      auth = ('tarenacode','code_2013')
    2. 下载笔记网站
      1. URL: http://code.tarena.com.cn/
      2. 正则: href=r'<a href="(.*?)/.*?</a>'
  4. SSL证书认证(verify)
    1. verify = True : 默认, 进行SSL证书认证
       verify = False: 不对URL做认证
       ** 针对于没有做证书认证的 https 的网站 **
  5. timeout 
    超时异常
  
3. requests.post()
  1. requests.post(url,data=data)
  2. 多了data参数,是字典,是Form表单数据(不用编码)
4. 有道翻译破解案例(post)
----------------------------------------------
1. xpath 解析模块
  1. 在XML文档中查找信息的语言, 同样适用于HTML文档的检索
  2. xpath辅助工具
      1. chrome 插件: xpath Helper
      2. Firefox插件: xpath Checker
      3. xpath编辑工具: XML Quire
  4. xpath匹配演示
    1. 查找所有的book节点://book
    2. 查找所有book下title子节点中,lang属性值为'en'的节点
      //book/title[@lang='en']
    3. 查找bookstore下的第2个book节点下title子节点
      //bookstore/book[2]/title
    4. 查找所有book/title中lang属性的值
      //book/title/@lang
  5. 选取节点
    1. //: 所有节点中查找
          //price  //book   //price

    2. @: 获取节点属性值
          **条件: //div[@class="movie-item-info">]
          **取值: //div//a/@src
    3. |: 匹配多路径
          **  xpath表达式1 | xpath表达式2
  6. 函数
    1. contains()
      匹配一个属性值中包含某些字符串的节点
      //title[contains(@lang,'e')]
      //div[contains(@id,'qiushi_tag_')]
    2. text(): 获取文本
      //book/title/text()

  6. 函数
    1. contains()
      匹配一个属性值包含某些字符串的节点
      //title[contains(@lang,'e')]
      //div[contains(@id,'qiushi_tag_')]
    2. text(): 获取文本
      //book/title/text()
2. lxml库及xpath使用 
  2. 使用流程# r_list = etree.HTML(html).xpath('xpath表达式')
    1. 导入模块lxml.etree 
    from lxml import etree
    2. 创建解析对象
    parse_html = etree.HTML(html)
    3. 调用xpath匹配: r_list = parse_html.xpath('xpath表达式')

    r_list = etree.HTML(html).xpath('xpath表达式')
  *** 只要调用了xpath, 结果一定是列表 ***
3. 腾讯招聘案例(xpath)
  1. 基准xpath表达式: 匹配所有职位的节点对象(tr)
    //tr[@class="even"] | //tr[@class="odd"]
  2. for 循环拿出每一个节点对象, 做数据提取
    for tr in [节点对象1,节点对象2,...]:
      job_link = tr.xpath('./td[1]/a/@href')
      job_name = tr.xpath('./td[1]/a/text()')
      job_type = tr.xpath('./td[2]/text()')
      job_number = tr.xpath('./td[3]/text()')
      job_address = tr.xpath('./td[4]/text()')
      job_time = tr.xpath('./td[5]/text()')

    作业:
    糗事百科
      1. URL地址: 百度糗事百科 - 文本
      2. 目标
        1. 用户昵称
        2. 段子内容
        3. 好笑数量
        4. 评论数量
    ******
      1. 基准xpath, 匹配出所有段子的节点对象(contants)
      2. for循环......
    猫眼电影, 用xpath实现    