import allure

@allure.feature('商品模块')
class TestProduct:
    @allure.story('商品查询')
    @allure.title('所有商品查询')
    def test_get_all(self,anonymous):
        with allure.step('get /products'):
            resp=anonymous.get('/products')
        with allure.step('断言状态码 200'):
            assert resp.status_code == 200
        with allure.step('断言响应包含products字段且不为空'):
            assert 'products' in resp.json()
            assert len(resp.json()['products']) > 0
            allure.attach(str(resp.json()['total']),'商品总数',allure.attachment_type.TEXT)


    @allure.title('查询单个商品')
    def test_get_one(self,anonymous):
        with allure.step('获取商品ID=1'):
            resp=anonymous.get('/products/1')
        with allure.step('断言状态码 200且ID匹配'):
            assert resp.status_code == 200
            assert resp.json()['id']==1