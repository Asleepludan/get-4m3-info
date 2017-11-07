# -*- coding:utf-8 -*-
"""
URL: http://4m3.tongji.edu.cn/
“统一身份认证” button xpath: //*[@id="login_box"]/div[2]/div/h2/a
Description: get information from 4m3.tongji.edu.cn, only get lines with 'new' in them
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import signal


class Get4m3Info:
    def __init__(self):
        self.url = "http://4m3.tongji.edu.cn/"
        self.username = 'xxxxxx'
        self.passward = 'xxxxxx'

    def get_4m3_info(self):
        # 模拟登陆4m3
        print "begin 4m3"
        driver = webdriver.PhantomJS()
        try:
            driver.get(self.url)
        except:
            message = 'get 4m3 website error\n'
            return message

        elem = driver.find_element_by_xpath('//*[@id="login_box"]/div[2]/div/h2/a')  # 选取“统一身份认证”按钮
        elem.send_keys(Keys.ENTER)  # 登入
        time.sleep(0.5)

        # 用户名 密码
        elem_user = driver.find_element_by_name("Ecom_User_ID")
        elem_user.send_keys(self.username)
        elem_pwd = driver.find_element_by_name("Ecom_Password")
        elem_pwd.send_keys(self.passward)
        elem_login = driver.find_element_by_name("submit")
        elem_login.send_keys(Keys.ENTER)
        time.sleep(0.5)

        # 尝试获取网页上的文字信息
        i = 2
        message = '4m3:\n'
        while 1:
            xpath = '/html/body/table/tbody/tr/td[3]/div/div/div/table/tbody/tr[' + str(i)+']'
            text = driver.find_element_by_xpath(xpath).text
            if 'new' not in text:
                message = message + '\n'
                break
            my_text = text[0:text.rfind('new')-1]
            message = message + my_text + '\n'
            i = i+1

        driver.service.process.send_signal(signal.SIGTERM)
        driver.quit()
        print "quit 4m3"
        return message




