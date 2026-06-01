import requests
from common.config import BASE_URL
from common.logger import get_logger

logger=get_logger()

class ApiClient:
    """需要登录"""
    def __init__(self):
        self.session=requests.Session()
        self.token=None

    def login(self,username,password):
        url=f"{BASE_URL}/auth/login"
        data={'username':username,'password':password}

        logger.info(f"正在登录{username}账户")
        resp=self.session.post(url,json=data)

        if resp.status_code==200:
            self.token=resp.json()['accessToken']
            """将token放入请求头"""
            self.session.headers.update({
                "Authorization":f"Bearer {self.token}"
            })
            logger.info(f"登录成功，token已加入请求头")
        else:
            logger.info(f"登录失败，状态码{resp.status_code}")
        return resp

    def get(self,path,**kwargs):
        url=f"{BASE_URL}{path}"
        logger.info(f"get {url}")
        return self.session.get(url,**kwargs)

    def post(self,path,**kwargs):
        url=f"{BASE_URL}{path}"
        logger.info(f"post {url}")
        return self.session.post(url,**kwargs)

    def put(self,path,**kwargs):
        url=f"{BASE_URL}{path}"
        logger.info(f"put {url}")
        return self.session.put(url,**kwargs)

class AnonymousClient:
    """不用登录"""
    def get(self,path):
        return requests.get(f"{BASE_URL}{path}")