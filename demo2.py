import jsonpath
import pytest
import requests
"""
框架封装怎么做
"""

"""
数据文件常用的有 ：yaml[pyyaml] ,excel[pandas]
测试框架核心思路:
读数据 ——> 执行测试[发送请求，接受回答] ——> 断言 ——> 生成报告  
"""
# DDT数据驱动测试
# datas = xfile.read(r"D:\data\训练用例。xls").excel_to_dict(sheet=1)
# dic = {} 定义一个空字典存放公共数据
# @pytest.mark.parametrize("case_info",datas) 和for循环一个作用
# def test_excute(case_info):
#     应答 = requests.request(url=case_info["接口url"],
#                             method=case_info["请求方式"],
#                             data=case_info["JSON参数"],
#                             params=["URL参数"])
#    print(应答.json())
#    assert case_info["预期状态码"] == 应答.status_code
#    判断是否要提取返回结果的值 提取后存放到公共容器中如dic
#    if case_info["提取参数"]:
#    dic[case_info["提取参数"]] = jsonpath.jsonpath(应答.json(),case_info["提取参数"])[0]
def excute(method,url,data, params):
    应答 = requests.request(url=url,
                            method=method,
                            data=data,
                            params=params)#发送请求 参数化处理
    print(应答.json())

#调用函数 执行登录
excute(url="http://shop-xo.hctestedu.com/index.php?s=/api/user/login",
          method="post",
          params={"application":"app","application_client_type":"weixin"},
          data={"accounts":"huace_xm","pwd":"123456","type":"username"})
