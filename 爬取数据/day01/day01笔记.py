王伟超
  wangweichao@tedu.cn
    
1. 概述
  1. 网络爬虫(网络蜘蛛, 网络机器人)
    1. 定义: 抓取网络数据的程序
    2. 用python程序模仿人点击浏览器访问网站(尽可能真实的模仿人用浏览器访问)
    3. 目的: 获取大量的数据分析
  
  2. 企业获取数据的方式
    1. 公司自有数据
    2. 第三方数据平台购买
    3. 爬虫爬取数据: 市场上没有或价格太高的

  3. Python做爬虫优势
    1. 请求模块, 解析模块丰富成熟, 强大的Scrapy爬虫框架
    2. IO操作多, 多线程在爬虫可以发挥效率
    
    PHP: 对多线程, 异步支持不太好
    JAVA: 代码笨重, 代码量大
    C/C++: 虽然效率高, 但是代码成形慢
  
  4. 爬虫分类
    1. 通用网络爬虫(搜索引擎, 遵守robots协议)
      robots协议: 网站通过robots协议告诉搜索引擎哪些页面可抓, 哪些不可抓
      http://www.taobao.com/robot.txt
      https://www.jd.com/robots.txt      

    2. 聚焦网络爬虫
      自己写的爬虫程序

  5. 爬取数据的步骤
    1. 确定url地址4
    2. 发请求, 获取响应
    3. 解析响应内容
      1. 所需数据, 保存
      2. 页面中新的URL, 继续第二步

2. WEB回顾
  1. URL: 统一资源定位符
    scheme: //host:prot/path.../?query-string=123...#anchor
    协议       域名  端口 资源路径   查询参数            锚点
    # 多个查询参数之间要用 & 做分隔
    # anchor:  锚点 (跳转到网页指定的位置)
  2. HTTP 和 https 
    HTTP: 80
    HTTPS:443(HTTP+SSL),HTTP升级版, 加了SSL安全套接层, 在传输层对数据加密,
    保障数据安全
  3. 请求头(Request Headers)
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 # 反爬第一步, 浏览器的信息  可以搜索User-Agent 大全
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8 # 权重值
    Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2 # 权重值
    Accept-Encoding: gzip, deflate, br# 是否支持解压缩
    Referer: https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E6%95%B0%E6%8D%AE%E5%A0%82&oq=gif&rsv_pq=f13a17d500062774&rsv_t=71b5gZwbXQc9LlnDDu0nqp08mjAWwACCkCKktDBadPIJN9u%2FGBsuNdxzKIA&rqlang=cn&rsv_enter=1&inputT=2802&rsv_sug3=15&rsv_sug1=12&rsv_sug7=100&rsv_sug2=0&prefixsug=shujutang&rsp=0&rsv_sug4=4111
    Connection: keep-alive # 是否支持长连接
    Cookie: BAIDUID=9F3CA675C1B538AC5DAEA7B73CAA6495:FG=1; BIDUPSID=1445355B72B087408943B62B70A6EC36; PSTM=1553824147; BD_UPN=133352; H_PS_PSSID=1429_21086_28772_28723_28558_28697_28585_28640_26350_28603_28625_28606; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; PSINO=3; H_PS_645EC=5de9o%2BaGfHRp8d0iye1mhW1%2Ftn1AX67pRZGgXqJ9lp8aXbFDwqjoki%2F0H1Q; BD_HOME=0
    Upgrade-Insecure-Requests: 1 # 是否自动升级为HTTPS
    Cache-Control: max-age=0 # max-age>0代表直接从浏览器缓存中提取
  4. GET 和 POST 
    1. GET: 查询参数在URL地址上显示出来
    2. POST: Form表单提交, 传输大文本, 数据隐藏在Form表单

3. 请求模块(urllib.request) 
  1. urllib.request.urlopen('URL地址')方法:  # 可以放url字符串,也可以放request对象
    1. 作用: 向网站发起请求并获取响应对象
      read方法: 得到的是字节串, 需要再解码
      response = urlopen('http://www.baidu.com/')
      html = response.read().decode()
      得到http内容
    2. 问题: urlopen方法不支持重构User-Agent

  2. urllib.request.Request('URL',headers{}) # 建立request 对象喂给urlopen方法
    1. 创建请求对象
      request = urllib.request.Request('http://www.baidu.com/',headers={"User-Agent":""})
    2. 发请求获取响应对象
      response = urllib.request.urlopen(request)
    3. 获取响应内容
      html = response.read().decode()

    # 返回http响应码
    print(response.getcode())
  
  3. 响应对象(response)方法
    1. read()
    2. getcode(): 返回HTTP响应码
      200: 成功
      302: 临时转移至新的URL
      404: 页面未找到
      500: 服务器出错

4. 编码模块(urllib.parse)
  1. urllib.parse.urlencode({})
    key = {'图片':'美女'}
    示例(03-urlencode.py): 在终端输入搜索内容, 得到搜索结果, 保存到本地文件
  
  2. quote()   urllib.parse.quote('字符串')
    string = urllib.pares.quote('冯绍峰')
    string =='%E5%86%AF%E7%BB%8D%E5%B3%B0'
    url = 'http://www.baidu.com/s?wd=%s'%string

  3. unquote()

5. 
  2. 步骤
    第一页: http://tieba.baidu.com/f?kw=?&pn=0
    第二页: http://tieba.baidu.com/f?kw=?&pn=50
6. 百度贴吧数据抓取
7. 正则解析模块(re)
  1. re模块使用流程
    1. 写法1: r_list = re.findall('正则表达式','字符串',re.S)
    2. 写法2
      1. 创建编译对象
        p = re.compile('正则表达式',re.S)
      2. 进行字符串匹配
      r_list = p.findall('字符串')
  2. 元字符
    . : 匹配任意一个字符(不包括\n) re.S
    \d: 1个数字
    \s: 空白字符  
    \S: 非空白字符  
    []: 包含[]内容
    \w: 普通字符
    \W: 特殊字符

    *: 0次到多次
    +: 1次到多次
    ?: 0次到1次
    {m}: m次
    {m,n}: m次到n次
  3. 贪婪匹配, 非贪婪匹配
    贪婪匹配(.*): 在整个表达式匹配成功的前提下, 尽可能多的去匹配每串符串
    非贪婪匹配(.*?): 在整个表达式匹配成功的前提下,尽可能少的去匹配每串字符
     
作业：
  1、把百度贴吧案例重新写一遍,不要参照课上代码
  2、爬取猫眼电影信息：猫眼电影 - 榜单 - top100榜
     猫眼电影-第1页.html
     猫眼电影-第2页.html
     ...
  3、正则回顾、pymysql回顾、pymongo回顾、MySQL和MongoDB基本命令回顾
  
