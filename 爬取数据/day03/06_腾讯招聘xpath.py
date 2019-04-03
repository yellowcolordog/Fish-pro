from lxml import etree

def parse_job_info(html):
    job_info_list=etree.HTML(html).xpath('//tr[@class="even"]|//tr[@class="odd"]')
    for tr in job_info_list:
        job_link = "http://hr.tencent.com/"+tr.xpath('./td[1]/a/@href')[0]
        job_name = tr.xpath('./td[1]/a/text()')[0]
        job_type = tr.xpath('./td[2]/text()')[0]
        job_number = tr.xpath('./td[3]/text()')[0]
        job_address = tr.xpath('./td[4]/text()')[0]
        job_time = tr.xpath('./td[5]/text()')[0]
