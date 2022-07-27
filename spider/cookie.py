# -*- coding: utf-8 -*-

import os
import time
from configs.config import username,password,log
from utils.browser import Browser

"""cookie的生成及保存"""

class Cookie(Browser):

    def __init__(self):
        self.username = username
        self.password = password

    def get_cookie(self):
        """
        获取cookie
        :return:
        """
        self.get_dirver(False)
        index_url = 'https://www.1688.com/'
        self.driver.get(index_url)
        log.info("正在为获取cookie做初始化")
        time.sleep(8)
        current_url = self.driver.current_url
        # current_url = 'login.1688.com'
        log.info(current_url)
        if 'login' in current_url:
            self.driver.quit()
            log.info("需要登录，开始登录！")
            cookie = self.login_1688()
        else:
            log.info("开始获取cookie")
            cookie = self.cookie_str()
        self.save_data('./data/cookie.txt', cookie)

        return cookie

    def cookie_str(self):
        """cookie转为string"""
        cookies = ''
        list_cookies = self.driver.get_cookies()  # 这里返回的是一个更多信息的字典列表
        for i in list_cookies:
            cookies += f"{i['name']}={i['value']};"
        log.info(cookies)
        self.driver.quit()
        return cookies

    def login_1688(self):
        """
        1688的登录，暂未遇到，暂时先预留，
        爬取频繁可能会出现要登录的
        """
        self.get_dirver(False)
        self.driver.get('https://login.1688.com')
        time.sleep(3)
        iframe = '#loginchina > iframe'
        username_css = '#fm-login-id'
        password_css = '#fm-login-password'
        # driver.switch_to.frame(
        #     driver.find_element_by_css_selector(iframe) # //*[@id="fm-login-id"]
        # )
        # try:
        element = self.driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys(self.username)
        time.sleep(3)
        element = self.driver.find_element_by_css_selector(password_css).send_keys(self.password)
        time.sleep(3)
        self.driver.find_element_by_css_selector(
            "#login-form > div.fm-btn"
        ).click()
        time.sleep(10)
        # except:
        #     log.error("输入账号密码遇到异常，请手动完成登录")
        #     time.sleep(10)
        # input('是否需要或者已完成验证码输入，已完成验证码请按回车键！')
        # cookies = self.cookie_str()
        # return cookies


    def save_data(self,file_path,content):
        """
        保存数据，此处主要用于保存cookie
        :param file_path:
        :param content:
        :return:
        """
        try:
            with open(file_path,'w') as f:
                f.write(str(content))
        except:
            with open('../data/cookie.txt','w') as f:
                f.write(str(content))


# Cookie().login_1688()

