import allure
from common.api_client import ApiClient

@allure.feature('异常场景测试')
class TestException:
    @allure.story('鉴权')
    @allure.title('未登录访问需要 token 的接口')
    def test_no_token(self,anonymous):
        with allure.step('使用未登录用户访问/auth/me'):
            resp=anonymous.get('/auth/me')
        with allure.step('断言返回未授权状态码401/403'):
            assert resp.status_code in (401, 403)
            allure.attach(str(resp.status_code),'实际响应',allure.attachment_type.TEXT)


    @allure.title('使用错误token')
    def test_invalid_token(self):
        with allure.step('创建一个客户并设置错误token'):
            client=ApiClient()
            client.session.headers['Authorization']='Bearer wrong_token'
        with allure.step('访问/auth/me'):
            resp=client.get('/auth/me')
        with allure.step('断言返回401/403'):
            assert resp.status_code in (401, 403)