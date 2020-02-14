import pytest
import api

from api.api_employee import Employee
from tools.assert_tools import assert_tool
from tools.get_log import GetLog
from tools.read_json import read_json

#
class Test_Employee:

    def setup(self):
        self.emp = Employee()
        self.log = GetLog.get_logger()

    @pytest.mark.parametrize('username,mobile,workNumber',read_json('add_emp.json'))
    def test_01_add(self,username,mobile,workNumber):
        r = self.emp.add_emp(username,mobile,workNumber)
        self.log.info("添加员工接口返回信息：{}".format(r.json()))
        # 获取 ID 值
        id = r.json().get('data').get('id')
        api.user_id = id
        self.log.info("ID值：{}".format(id))
        assert_tool(r)

    def test_02_update(self):
        r = self.emp.update_emp("xxxiii-new")
        self.log.info("修改员工接口返回信息：{}".format(r.json()))
        assert_tool(r)

    def test_03_search(self):
        r = self.emp.search_emp()
        self.log.info("查询员工接口返回信息：{}".format(r.json()))
        assert_tool(r)

    def test_04_delete(self):
        r = self.emp.delete_emp()
        self.log.info("删除员工接口返回信息：{}".format(r.json()))
        assert_tool(r)

