import re

html = """
<div><p>九霄龙吟惊天变</p></div>
<div><p>风云际会潜水游</p></div>
"""
# 贪婪匹配
p = re.compile('<div>.*</div>',re.S)
l = p.findall(html)
print(l)

# 非贪婪匹配
p = re.compile('<div>.*?</div>',re.S)
l = p.findall(html)
print(l)