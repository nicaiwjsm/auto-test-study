自动化测试学习记录・第 1 天
学习方向：接口自动化测试入门
📚 今日学习内容
掌握 Python + Requests 实现基础接口请求
完成商城项目登录 POST 接口调用实战
熟悉接口响应结果断言写法，校验返回字段
学习 jsonpath 语法，精准提取接口 token 鉴权参数
实现登录鉴权 -> 携带 Token 调用业务接口完整流程
💻 实战源码
python
运行
import jsonpath
import requests

# 1. 调用用户登录接口
response_login = requests.request(
    url="http://shop-xo.hctestedu.com/index.php?s=/api/user/login",
    method="post",
    params={"application":"app","application_client_type":"weixin"},
    data={"accounts":"huace_xm","pwd":"123456","type":"username"}
)

# 打印登录接口返回数据
print(response_login.json())

# 接口结果断言校验
assert "登录成功" == response_login.json()["msg"]
assert "28" == response_login.json()["data"]["id"]
assert "huace_xm" == response_login.json()["data"]["username"]

# 2. jsonpath全局匹配提取token令牌
token = jsonpath.jsonpath(response_login.json(), "$..token")[0]
print(f"成功提取登录令牌：{token}")

# 3. 携带token调用商品收藏接口
response_collect = requests.request(
    url=f"http://shop-xo.hctestedu.com/index.php?s=/api/goods/favor&token={token}",
    method="post",
    params={"application":"app","application_client_type":"weixin"},
    data={"id":"12"}
)

# 打印收藏接口返回数据
print(response_collect.json())
✅ 今日学习成果
熟练使用 Requests 库发送 POST 类型接口请求
能够通过断言完成接口返回数据正确性校验
灵活运用 jsonpath 提取多层嵌套 JSON 字段
掌握接口核心关联思想，完成登录鉴权业务流程
⚠️ 问题总结
代码全程无报错，接口调用正常，流程运行稳定。
📝 后续学习规划
学习接口测试用例规范化编写
掌握接口请求参数封装与数据驱动
深入学习多接口串联实战、异常场景测试
逐步接入 Pytest 测试框架统一管理用例
