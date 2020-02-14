# 断言方法
def assert_tool(reponse,
                status_code=200,
                success=True,
                code=10000,
                message='操作成功！'):
    assert status_code == reponse.status_code
    assert success == reponse.json()["success"]
    assert code == reponse.json()["code"]
    assert message == reponse.json()['message']
