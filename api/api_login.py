import requests
import api
from tools.get_log import GetLog


class Login(object):

    def __init__(self):
        self.login_url = api.host + "/api/sys/login"
        self.log = GetLog.get_logger()

    def login(self,mobile,password):
        data = {"mobile":mobile, "password":password}
        self.log.info("登录数据为：{}".format(data))
        self.log.info("登录接口：URL:{},信息头:{}".format((self.login_url),(api.headers)))
        return requests.post(url=self.login_url,headers=api.headers,json=data)
