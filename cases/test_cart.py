import allure

@allure.feature('购物车模块')
class TestCart:
    @allure.story('获取购物车')
    def test_get_carts(self,anonymous):
        with allure.step('获取购物车所有'):
            resp=anonymous.get('/carts')
        assert resp.status_code == 200
        allure.attach(str(resp.json().get('total',0)),'购物车总数',allure.attachment_type.TEXT)

    @allure.story('往购物车添加商品')
    def test_add_cart(self,api_client):
        with allure.step('取第一个商品'):
            p_resp=api_client.get('/products')
            assert p_resp.status_code==200
            pid=p_resp.json()['products'][0]['id']
            allure.attach(str(id),'商品ID',allure.attachment_type.TEXT)

        with allure.step('添加到购物车'):
            payload={
                'userId':1,
                'products':[{'id':pid,'quantity':1}]
            }
            resp=api_client.post('/carts/add',json=payload)

            with allure.step('断言添加成功，且购物车包含该商品'):
                assert resp.status_code==201
                cart=resp.json()
                assert 'id' in cart
                assert cart['products'][0]['id']==pid
                allure.attach(str(cart['id']),'购物车ID',allure.attachment_type.TEXT)