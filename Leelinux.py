import requests
import json
class LeeLinux:
    def __init__(self):
        self.url = 'http://jsondata.25pp.com/index.html'
    def getJson(self,pageIndex):
        data = {'dcType': 0, 'resType': 1, 'listType': 5, 'catId': 0, 'clFlag': 1, 'perCount': 32, 'page': pageIndex}
        headerInfo = {'Host':'jsondata.25pp.com', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/601.5.17 (KHTML, like Gecko)\r\n', 'Accept': 'text,/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3', 'Accept-Encoding': 'gzip, deflate', 'Tunnel-Command': '4261433392', 'Content-Type': 'application/json', 'Referer':'http://ppmac2.25pp.com/zb_pp_v3/index.html', 'Content-Length': '87', 'Origin': 'http://ppmac2.25pp.com','Connection': 'keep-alive'}
        jLoad = json.dumps(data)
        req = requests.post(self.url, headers=headerInfo, data=jLoad)
        print req.status_code
        return req.text
    # def





