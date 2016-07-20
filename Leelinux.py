import urllib
import urllib2
import sys

class LeeLinux:
    def __init__(self):
        self.url = 'http://jsondata.25pp.com/index.html'
    def getJson(self,pageIndex):
        data = {'dcType':0,'resType':1,'listType':5,'catId':0,'clFlag':1,'perCount':32,'page':pageIndex}
        metaData = urllib.urlencode(data)
        header = {'Host':'jsondata.25pp.com','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0','Accept':'text,/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3','Accept-Encoding':'gzip, deflate','Tunnel-Command':'4261433392','Content-Type':'application/json','Referer':'http://ppmac2.25pp.com/zb_pp_v3/index.html','Content-Length':'87','Origin:http':'//ppmac2.25pp.com','Connection':'keep-alive'}
        metaHeader = urllib.urlencode(header)
        req = urllib2.Request(self.url,metaData,metaHeader)
        r = urllib2.urlopen(req)
        html=r.read()
        receive_header = r.info()
        html = html.decode('utf-8','replace').encode(sys.getfilesystemencoding())
        print receive_header
        print '#############'
        print html
        print req
        return req
















