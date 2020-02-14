import api
import requests

from tools.get_log import GetLog


class Employee(object):

    def __init__(self):
        self.add_url = api.host + '/api/sys/user'
        self.employee_url = api.host + '/api/sys/user/{}'
        self.log = GetLog.get_logger()

    def add_emp(self,username,mobile,workNumber):
        # data = {"username": "xxxiii",  "mobile": "16700001111","workNumber": "35456"}
        data = {"username": username,  "mobile": mobile,"workNumber": workNumber}
        self.log.info("添加员工信息：{}".format(data))
        self.log.info("添加员工接口：URL:{},信息头:{}".format((self.add_url),(api.headers)))
        return requests.post(url=self.add_url,headers=api.headers,json=data)

    def update_emp(self,username):
        # data = {"username":"xxxiii-new"}
        data = {"username":username}
        self.log.info("修改员工信息：{}".format(data))
        self.log.info("修改员工接口：URL:{},信息头:{}".format((self.employee_url.format(api.user_id)),(api.headers)))
        return requests.put(url=self.employee_url.format(api.user_id),headers=api.headers,json=data)

    def search_emp(self):
        self.log.info("查询员工接口：URL:{},信息头:{}".format((self.employee_url.format(api.user_id)), (api.headers)))
        return requests.get(url=self.employee_url.format(api.user_id),headers=api.headers)

    def delete_emp(self):
        self.log.info("删除员工接口：URL:{},信息头:{}".format((self.employee_url.format(api.user_id)), (api.headers)))
        return requests.delete(url=self.employee_url.format(api.user_id),headers=api.headers)