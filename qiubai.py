# -*- coding:utf-8 -*-

import urllib2
import re
class QSBK:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6"
        self.headers = {"User-Agent": self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self, pageIndex):
        try:
            url = "https://www.qiushibaike.com/hot/page/" + str(pageIndex)
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode("utf-8")
            return pageCode
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"connected error, reason: ", e.reason
                return None

    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "loading failed..."
            return None
        else:
            pattern = re.compile(r'<div class="content">.*?<span>(.*?)</span>.*?</div>', re.S)
            items = re.findall(pattern, pageCode)
            pageStories = []
            for item in items:
                pageStories.append(item)
        return pageStories

    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStroies = self.getPageItems(self.pageIndex)
                if pageStroies:
                    self.stories.append(pageStroies)
                    self.pageIndex += 1

    def getOneStory(self, pageStories, page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == "q":
                self.enable = False
                return
            print story

    def start(self):
        print "start view QSBK, press Q to quit:"
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories, nowPage)

spider = QSBK()
spider.start()






