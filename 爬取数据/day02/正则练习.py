import re

html="""
  <div class="animal">
    <p class="name">
      <a title="Tiger"></a>
    </p>

    <p class="content">
      Two tigers two tigers run fast
    </p>
  </div>

  <div class="animal">
    <p class="name">
      <a title="Rabbit"></a>
    </p>
    
    <p class="content">
      Small white rabbit white and white
    </p>
  </div>
  """
p = re.compile(r'<div class="animal">.*?<a title="(.*?)"></a>.*?"content">\s*(.*?)\s*</p>.*?</div>',re.S)
l = p.findall(html)

for i in l:
    print('动物名称: %s'%i[0])
    print('动物描述: %s'%i[1])