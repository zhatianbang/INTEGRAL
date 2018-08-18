#coding:utf-8

from selenium import webdriver
import time
import unittest

class baidu(unittest.TestCase):
    """打开百度测试"""

    def setUp(self):
        self.driver = webdriver.Firefox()


    def test00001_open_baidu(self):
        """"第一个测试  打开百度、输入大美女"""
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id('kw').send_keys('大美女')
        self.driver.find_element_by_id('su').click()


    def test00002_open(self):
        """"第二个测试   打开百度、输入360"""
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('360')
        self.driver.find_element_by_id('su').click()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
