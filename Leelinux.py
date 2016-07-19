import urllib
import urllib2
import cookielib  

test_data={'dcType':0,'resType':1,'listType':5,'catId':0,'clFlag':1,'perCount':32,'page':1}
test_data_urlencode=urllib.urlencode(test_data)
headers={'Host':'jsondata.25pp.com', 
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0', 
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3', 
'Accept-Encoding':'gzip, deflate', 
'Tunnel-Command':'4261433392', 
'Content-Type':'application/json', 
'Referer':'http://ppmac2.25pp.com/zb_pp_v3/index.html', 
'Content-Length':'87', 
'Origin:http':'//ppmac2.25pp.com', 
'Connection':'keep-alive'}
headers_urlencode=urllib.urlencode(headers)
requrl='http://jsondata.25pp.com/index.html'
req=urllib2.Request(requrl,test_data_urlencode)
req.addheader(headers_urlencode)
print(req) 
res_data=urllib2.urlopen(req)
res=res_data.read()
print(res)


