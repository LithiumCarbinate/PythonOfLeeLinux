import urllib
import urllib2
import re
 

 # 
class Spider:
 
    def __init__(self):
        self.siteURL = 'http://ppmac2.25pp.com/zb_pp_v3/index.html#u_game_0_0_5_1'
 
    def getPage(self,pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        print url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')
 
    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
#<li class=""> <a title="The Economist on iPad " data-pos="2" class="fl app-icon" href="javascript:;" data-action="appdetail" data-appid="444524375" data-uid=""> <img src="http://zbimg.25pp.com/images/artwork/87/444524375_108x108.jpg" alt="The Economist on iPad " height="60" width="60"> <span class="cover cover60-white"></span>  <span class="cover icon-ipad3"></span>  </a> <h3><a title="The Economist on iPad " data-pos="2" href="javascript:;" data-action="appdetail" data-appid="444524375" data-uid="">The Economist on iPad </a></h3> <div class="down-count"><span>2576</span>人安装</div> <div class="btn-box">  <span data-name="setup" title="点击下载" class="fl icon icon-down" data-appid="444524375" data-uid=""></span> <span data-name="cancel" class="fl icon  icon-cancel01" title="点击取消下载" data-appid="444524375" data-uid=""></span>  </div>  <div class="dc-select pa" data-appid="444524375"> <strong>请选择设备</strong>  </div>  </li>
        pattern = re.compile('<span data-name="setup".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items = re.findall(pattern,page)
        for item in items:
            print item[0],item[1],item[2],item[3],item[4]
 
spider = Spider()
spider.getContents(1)

# <span data-name="setup" title="点击下载" class="fl icon icon-down" data-appid="1111479468" data-uid=""></span>