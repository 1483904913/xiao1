# -*- coding:utf-8 -*-
__author__ = 'pf'

import time
import requests


class Login:
    # 初始化
    def __init__(self):
        # 检测间隔时间，单位为秒
        self.every = 0.5

    # 模拟登录
    def login(self):
        print(self.getCurrentTime(), u"拼命连网中...")
 #       url = 'http://172.16.254.6/drcom/login?callback=dr1589985374636&DDDDD=13361653468%40telecom&upass=700899&0MKKey=123456&R1=0&R3=0&R6=0&para=00&v6ip=&_=1589985359545'
        url = 'http://172.16.254.6/drcom/login?callback=dr1589985374636&DDDDD=18146702513%40telecom&upass=512512&0MKKey=123456&R1=0&R3=0&R6=0&para=00&v6ip=&_=1589985359545'
        # 消息头
        headers = {
            'Host': '172.16.254.6',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'close',
            'Referer': 'http://172.16.254.6/a79.htm?isReback=1',
            'PHPSESSID': 'ut2q1fnsj2t0go70uj78f61ja6'
        }
        # 提交的信息
        try:
            r = requests.get(url, headers=headers)
            print(self.getCurrentTime(), u'连上了...现在开始看连接是否正常')
        except:
            print("error")

    # 判断当前是否可以连网
    @property
    def canConnect(self):
        try:
            q = requests.get('https://www.baidu.com',timeout=0.5)
            if (q.status_code == 200):
                return True
            else:
                return False
        except:
            print('error')

    # 获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))

    # 主函数
    def main(self):
        print(self.getCurrentTime(), u"Hi，欢迎使用自动登陆系统")
        while True:
            self.login()
            while True:
                can_connect = self.canConnect
                if not can_connect:
                    print(self.getCurrentTime(), u"断网了...")
                    self.login()
                else:
                    print(self.getCurrentTime(), u"一切正常...")

                time.sleep(self.every)
            time.sleep(self.every)


login = Login()
login.main()
