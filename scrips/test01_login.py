import pytest
import api

from api.api_login import Login

from tools.assert_tools import assert_tool
from tools.get_log import GetLog
from tools.read_yaml import read_yaml


class Test_Login:

    def setup(self):
        self.login = Login()
        self.log = GetLog.get_logger()

    @pytest.mark.parametrize('mobile,password',read_yaml('login.yaml'))
    def test_login(self,mobile,password):
        r = self.login.login(mobile,password)
        self.log.info("登录接口返回信息：{}".format(r.json()))
        assert_tool(r)
        # 提取 token 值，并追加到信息头中
        token = r.json()["data"]
        api.headers["Authorization"] = "Bearer " + token
        self.log.info("token值：{}".format(token))

