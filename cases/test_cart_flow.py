import allure

@allure.feature('完成购物流程测试')
class TestCartFlow:
    @allure.story('登录 → 获取商品 → 加入购物车 → 校验数量与商品信息')
    def test_full_cart_flow(self,api_client):
        with allure.step('获取商品列表，取出第一个商品id和title'):
            resp=api_client.get('/products')
            assert resp.status_code == 200
            products=resp.json()['products']
            pid=products[0]['id']
            ptitle=products[0]['title']
            allure.attach(f"商品ID：{pid}，标题：{ptitle}",'选中商品',allure.attachment_type.TEXT)

        with allure.step('将该商品加两个到购物车'):
            add_resp=api_client.post('/carts/add',json={
                'userId':1,
                'products':[{'id':pid,'quantity':2}],
            })
            assert add_resp.status_code == 201

        with allure.step('断言购物车中商品ID、标题、数量都正确'):
            cart=add_resp.json()
            assert cart['products'][0]['id']==pid
            assert cart['products'][0]['title']==ptitle
            assert cart['products'][0]['quantity']==2
            allure.attach(str(cart),'完整购物车响应',allure.attachment_type.JSON)

        with allure.step('记录日志：流程通过'):
            from common.logger import get_logger
            logger = get_logger()
            logger.info(f"完整购物流程测试通过，购物车ID：{cart['id']}")