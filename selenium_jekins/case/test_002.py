#coding:utf-8

from selenium import webdriver
import time
import unittest

class baidu(unittest.TestCase):
    """打开百度测试"""

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test00003_open_baidu(self):
        """"第三个测试   打开百度、输入大美女"""
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id('kw').send_keys('测试三')
        self.driver.find_element_by_id('su').click()
        print ('测试三')


    def test00004_open(self):
        """第四个测试"""
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('测试四')
        self.driver.find_element_by_id('su').click()
        print ('测试四')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
