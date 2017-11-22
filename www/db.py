# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
page = 1
url = "https://www.qiushibaike.com/hot/page/" + str(page)
user_agent = "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6"
headers = {"User-Agent":user_agent}

try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode("utf-8")
    pattern = re.compile(r'<div class="content">.*?<span>(.*?)</span>.*?</div>',re.S)
    items = re.findall(pattern, content)
    for item in items:
        print item


except urllib2.URLError, e:
    if hasattr(e, "code:"):
        print e.code
    if hasattr(e, "reason:"):
        print e.reason

