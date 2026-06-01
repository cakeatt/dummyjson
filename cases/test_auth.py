import allure
import pytest
import requests
import pandas as pd
from common.config import BASE_URL


def read_login_data():
    file_path="data/login_cases.xlsx"
    df=pd.read_excel(file_path)
    return df.to_dict('records')

@allure.feature('用户认证模块12')
class TestAuth:
    @allure.story('登录接口')
    @pytest.mark.parametrize('case',read_login_data())
    def test_login(self,case):
        url=f"{BASE_URL}/auth/login"
        data={
            'username':case['username'],
            'password':case['password']
        }
        with allure.step(f"用户名{case['username']}登录"):
            resp=requests.post(url,json=data)

        with allure.step(f"状态码断言{case['expect_status']}"):
            assert resp.status_code==case['expect_status']

        if resp.status_code==200:
            with allure.step('登录成功'):
                assert 'accessToken' in resp.json()
                allure.attach(resp.json()['accessToken'],'token',allure.attachment_type.TEXT)
        else:
            with allure.step("登录失败"):
                assert 'message' in resp.json()
                allure.attach(resp.json()['message'],'message',allure.attachment_type.TEXT)