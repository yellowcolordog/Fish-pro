Day01回顾
1. 请求模块(urllib.request)
  1. Request(url字符)
  2. urlopen(请求对象,url)

2. 响应方法
  1. res.read()
     res.read().decode()
  2. res.getcode()

3. 编码模块(urllib.parse)
  1. urlencode({})
    一个查询参数:{'kw':'美女'}
      #编码后: 'kw=%D3...'
    多个查询参数: {'kw':'美女','pn':30}
      #编码后: 'kw=%D3...&pn=30'
  2. quote('')
    key='屠龙刀'
    quote(key) #编码后:'%E5...'
  3. unquote('')
    s = '%E5...'
    unquote(s)  # 屠龙刀
4. 数据爬去步骤
  1. 找URL规律(拼接)
  2. 获取响应内容
  3. 保存
5. 正则分组
  1. 分组(想要抓取什么内容, 就加())
  2. 正则方法
    r_list = re.findall('',html,re.S)
    p = re.compile('',re.S)
    r_list = p.findall(html)
  3. 先按照整体匹配, 然后再提取括号
    如果有多个括号, 则以元组形式显示
    # [(1,2),('a','b'),('c','d')]
  4. 贪婪匹配:.*
     非贪婪匹配: .*?

****************************************************
Day02笔记
  1. 正则分组练习
  <div class='animal'>
    <p class='name'>
      <a title='Tiger'></a>
    </p>

    <p class='content'>
      Two tigers two tigers run fast
    </p>
  </div>

  <div class='animal'>
    <p class='name'>
      <a title='Rabbit'></a>
    </p>
    
    <p class='content'>
      Small white rabbit white and white
    </p>
  </div>
    1. 抓取[('Tiger','Two tigers....fast'),()]
    p = re.compile(r"<a title='(.*?)'></a>.*?'content'>(.*?)</p>")
    2. 动物名称: tigers
       动物描述: two tigers...
  ****************************

2. csv 模块使用流程
  1. 导入模块
    import csv
  2. 打开文件(xxx.csv)
    with open('xxx.csv','a')as f:
      # 1. 初始化写入对象
      writer = csv.writer(f)
      # 2. 写入数据     
      writer.writerow(['旭叔叔','39'])
  3. 注意: windows 下会出现空行, 使用new参数, 编码是encoding
    with open('老师.csv','a',newline='',encoding='') 多放两个参数
3. 猫眼电影top100榜单
  1. 网址: 猫眼电影 - 榜单 - top100榜
  2. 目标: 电影名称, 主演, 上映时间
  3. 保存: 本地csv文件
  4. 步骤
    1. 找URL规律
      第一页:
      第二页:
      第三页:
    2. 
4. 数据的持久化存储
  1. pymongo回顾
    三个对象: 数据库连接对象, 创建库对象, 创建集合对象
    1. conn = pymongo.MongoClient('ip地址',27017)
    2. db = conn['库名']
    myset = db['table']
    myset.insert_one(dict)
    >>>show dbs
    >>>use 库名
    >>>show collections
    >>>db.集合名.find().pretty()
    >>>db.集合名.count()
    >>>db.dropDatabase()
  2. pymysql回顾
    1. 创建连接对象: db = pymysql.connect(...)
    2. 创建游标对象: cursor = db.xceul
    3. 执行命令: 提交到数据监控执行
    4. 提交到数据库执行
    5. 关闭 
    # 过滤警告
    import warnings
5. 猫眼电影存入mysql数据库
create databaseif it not except  maoyandb charset utf8;
===========================
6. requests模块
  1. 安装
    sudo pip3 install requests
    windows: python -m install requests
  2. requests.get(url,headers=headers)
    向网站发起请求, 并获取响应对象
  3. 响应对象:res 的方法属性:
    1. res.text: 获取响应内容(字符串)
    2. res.content: 获取响应内容(bytes)
    3. res.status_code: HTTP响应码
    4. res.encoding : 编码格式   默认需要改为'utf-8'
  4. 非结构化数据爬取
    html= res.content
    with open('赵丽颖.jpg','wb') as f:
      f.write(html)
      
7. 抓取腾讯招聘案例
  1. 网址: 腾讯招聘 - 社会 - 搜索
  2. 目标:
    *** 一级界面 *** # https://hr.tencent.com/position.php?keywords=&tid=0&lid=2268&start=0#a
      # <tr class="even">
      #   <td class="l square"><a target="_blank" href="position_detail.php?id=46719&amp;keywords=python&amp;tid=87&amp;lid=2268">CSIG15-自然语言研究员</a></td>
      #   <td>技术类</td>
      #   <td>1</td>
      #   <td>成都</td>
      #   <td>2019-04-02</td>
      # </tr>
      # <tr class="odd">
      #     <td class="l square"><a target="_blank" href="position_detail.php?id=46711&amp;keywords=python&amp;tid=87&amp;lid=2268">CSIG15-自然语言处理工程师</a></td>
			# 		<td>技术类</td>
			# 		<td>1</td>
			# 		<td>成都</td>
			# 		<td>2019-04-02</td>
      #   </tr>
      # r'<td class="l square">.*?href="(.*)">(.*?)</a>.*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>'
    1. 职位名称
    2. 职位类别
    3. 招聘人数
    4. 招聘地点
    5. 发布时间
    6. 职位连接
    *** 二级界面 *** # https://hr.tencent.com/position_detail.php?id=41853&keywords=&tid=0&lid=2268
      # <td colspan="3" class="l2">
      #   <div class="lightblue">工作职责：</div>
      #   <ul class="squareli">
      #     <li>负责移动游戏自动化测试工具的开发、维护和完善；</li>
      #     <li>负责移动游戏专项测试工具的开发、用例设计和测试执行；</li>
      #     <li>负责游戏整体的质量把控，制定测试方案、计划、跟踪实施，监控项目外网质量并实施改进； </li>
      #     <li>负责收集和分析业务测试需求，探索更多的测试手段和维度，帮助提升部门的测试质量、效率和深度。</li>
      #   </ul>
      # </td>
            
    r'<tr class="c">.*ul class="squareli"'
    7. 岗位职责
    8. 工作要求
  3. 实现步骤
    1. 找URL规律
    2. 一级页面正则表达式 
    3. 二级页面正则表达式
    4. 设计程序框架

作业: 
  1. 腾讯招聘二级子界面爬取, csv,mongodb,mysql
  2. 把昨天的课用requests重写
  3. 爬链家二手房
    目标: 房名称 价格 