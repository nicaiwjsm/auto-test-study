# auto-test-study
自动化测试学习记录 - 第 1 天（接口自动化入门）
学习内容
Python + Requests 接口自动化测试基础
发送 POST 请求，完成用户登录接口测试
学习接口响应结果断言（msg、id、username）
学习使用 jsonpath 提取响应中的 token 数据
携带 token 调用商品收藏接口实战
实战代码
python
运行
import jsonpath
import requests

# 1. 用户登录接口
应答 = requests.request(
    url="http://shop-xo.hctestedu.com/index.php?s=/api/user/login",
    method="post",
    params={"application":"app","application_client_type":"weixin"},
    data={"accounts":"huace_xm","pwd":"123456","type":"username"}
)

print(应答.json())

# 断言响应结果
assert "登录成功" == 应答.json()["msg"]
assert "28" == 应答.json()["data"]["id"]
assert "huace_xm" == 应答.json()["data"]["username"]

# 2. 使用 jsonpath 提取 token
token = jsonpath.jsonpath(应答.json(), "$..token")[0]
print("提取到的token：", token)

# 3. 携带token调用收藏接口
收藏应答接口 = requests.request(
    url="http://shop-xo.hctestedu.com/index.php?s=/api/goods/favor&token="+token,
    method="post",
    params={"application":"app","application_client_type":"weixin"},
    data={"id":"12"}
)

print(收藏应答接口.json())
学习成果
掌握 Requests 发送 POST 请求方式
学会对接口响应结果进行断言校验
掌握 jsonpath 提取接口返回数据中的 token
完成登录 → 提取鉴权信息 → 调用业务接口的流程
遇到的问题
无（运行成功）
明日计划
继续学习接口自动化测试，学习数据驱动、用例封装、接口关联等进阶内容
