import re

p = re.compile(r'<td class="l square">.*?href="(.*?)">(.*?)</a>.*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>',re.S)
html ="""
<tr class="even">
  <td class="l square"><a target="_blank" href="position_detail.php?id=46719&amp;keywords=python&amp;tid=87&amp;lid=2268">CSIG15-自然语言研究员</a></td>
  <td>技术类</td>
  <td>1</td>
  <td>成都</td>
  <td>2019-04-02</td>
</tr>
<tr class="odd">
    <td class="l square"><a target="_blank" href="position_detail.php?id=46711&amp;keywords=python&amp;tid=87&amp;lid=2268">CSIG15-自然语言处理工程师</a></td>
		<td>技术类</td>
		<td>1</td>
		<td>成都</td>
		<td>2019-04-02</td>
  </tr>
"""

l = p.findall(html)
print(l)