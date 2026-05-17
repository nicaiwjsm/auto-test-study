#    框架的主入口
import pytest,os
if __name__ == '__main__':
    pytest.main(["-vs",
                    "--capture=sys",  #捕获输出
                    "test_framework.py",
                    "clean-alluredir",  #执行前清空测试结果文件夹
                    "--alluredir=allure-result"  #测试结果保存的文件夹
                    ])
    os.system("allure generate allure-result -o ./report_allure --clean")