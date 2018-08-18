# 参考文档：http://www.cnblogs.com/yoyoketang/p/7744538.html
# 参考代码：https://github.com/yoyoketang/selenium_report/，下面的附件中应该也有代码压缩包
#
# #以下代码主要copy上面的
# 主要优点有
# 1.兼容Python2和3
# 2.汉化
# 3.带饼图
# 4.失败重跑机制
# 5.异常截图


# coding:utf-8
import unittest
import os,time
import HTMLTestRunner_jpg

# python2.7要是报编码问题，就加这三行，python3不用加
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

cur_path = os.path.dirname(os.path.realpath(__file__))#获取当前脚本的工程目录
case_path = os.path.join(cur_path, "case")        # 测试用例的路径
report_path = os.path.join(cur_path, "report")  # 报告存放路径

if __name__ == "__main__":
    discover = unittest.defaultTestLoader.discover(case_path,"test*.py")
    """如果有多个discovery，可以利用测试套件
    all = unittest.TestSuite()
    all.addTests(discover)
    然后 run.run(all)即可"""
    print(discover)
    #now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = report_path+"\\"+"result.html"
    fp =open(filename, "wb")

    run = HTMLTestRunner_jpg.HTMLTestRunner(title="可以装逼的测试报告",
                                            description="测试用例参考description",
                                            stream=fp,
                                            retry=1)

    run.run(discover)
    fp.close()