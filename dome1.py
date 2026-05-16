import jsonpath
import requests

应答 = requests.request(url="http://shop-xo.hctestedu.com/index.php?s=/api/user/login",
                     method="post",
                     params={"application":"app","application_client_type":"weixin"},
                     data={"accounts":"huace_xm","pwd":"123456","type":"username"})

print(应答.json())
assert "登录成功" == 应答.json()["msg"]
assert "28" == 应答.json()["data"]["id"]
assert "huace_xm" == 应答.json()["data"]["username"]

"""
1.获取方式:用JSON数据都Key获取
token = 应答.json()["data"]["token"]
2.jsonpath获取
明确知道在哪就$.Key
不知道的就$..key
"""
token = jsonpath.jsonpath(应答.json(),"$..token")[0]
print(token)

收藏应答接口 = requests.request(url="http://shop-xo.hctestedu.com/index.php?s=/api/goods/favor&token="+token,
                            method="post",
                            params={"application":"app","application_client_type":"weixin"},
                                data={"id":"12"})
print(收藏应答接口.json())

"""
加密接口
ens=EncryptDate("123456785678")
username = ens.encrypt("huace_xm")
print(username)
"""


