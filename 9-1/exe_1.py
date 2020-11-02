import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

username = "13223543593"
password = "a12345678"

CJY_username = "2901291002"
CJY_password = "a12345678"
CJY_ID = "2e6cadc5703b4ad419f0798b3521f6e8"
CJY_KIND = 9102

#!/usr/bin/env python
# coding:utf-8

import requests
from hashlib import md5

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

# 简书验证
class CracToucClick():
    def __init__(self):
        self.url = "http://www.jianshu.com/sign_in"
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser,20)
        self.username = username
        self.password = password
        self.CJY = Chaojiying_Client(
            CJY_username,
            CJY_password,
            CJY_ID,
        )

    def open(self):
        '''
        打开网页输入用户名密码
        :param self:
        :return: None
        '''
        self.browser.get(self.url)# 打开网页
        # 定位账号密码输入框
        username = self.wait.until(EC.presence_of_element_located((By.ID,"session_email_or_mobile_number")))
        password = self.wait.until(EC.presence_of_element_located((By.ID,"session_password")))
        # 输入内容
        username.send_keys(self.username)
        password.send_keys(self.password)

    def get_touclick_button(self):
        '''
        获取初始验证按钮，加载验证码图片
        :param self:
        :return:
        '''
        button = self.wait.until(EC.presence_of_element_located((By.ID,"sign-in-form-submit-btn")))
        return button

    def get_touclick_element(self):
        '''
        获取验证码图片对象
        :param self:
        :return:
        '''
        element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,"geetest_widget")))
        return element

    def get_position(self):
        '''
        获取验证码图片位置
        :param self:
        :return: 位置的元组
        '''
        element = self.get_touclick_element()
        time.sleep(2)
        location = element.location
        size = element.size
        top,bottom,left,right = location['y'],location['y']+size['height'],location['x'],location['x']+size['width']
        top = int(top)
        bottom = int(bottom)
        left = int(left)
        right = int(right)

        return (top,bottom,left,right)

    def get_screenshoot(self):
        '''
        网页截图
        :return:
        '''
        screenshoot = self.browser.get_screenshot_as_png()
        screenshoot = Image.open(BytesIO(screenshoot))
        return screenshoot

    def get_touclick_image(self,name = "captcha.png"):
        '''
        获取图片
        :param name:
        :return:
        '''
        top, bottom, left, right = self.get_position()
        print("验证码的位置",top,bottom,left,right)
        # 获取截图对象
        screenshoot = self.get_screenshoot()
        captcha = screenshoot.crop((left,top,right,bottom))
        captcha.save(name)

        return captcha

    def get_points(self,captcha_result):
        '''
        解析识别结果
        :param captcha_result:
        :return:
        '''
        groups = captcha_result.get("pic_str").split("|")
        locations = [[int(number) for number in group.split(",")] for group in groups]
        print("locations",locations)
        return locations

    def touch_click_words(self,locations):
        '''
        点击
        :param location:
        :return:
        '''
        for location in locations:
            print(location)
            ActionChains(self.browser).move_to_element_with_offset(
                self.get_touclick_element(),
                location[0],
                location[1]
            ).click().perform()# click操作 perform执行
            time.sleep(1)

    def touch_click_verify(self):
        '''
        点击验证码
        :return:
        '''
        botton = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,"geetext_commit")))
        botton.click()

    def login(self):
        '''
        登录
        :return:
        '''
        submit = self.wait.until(EC.presence_of_element_located((By.ID,"_submit")))
        submit.click()
        time.sleep(10)
        print("登陆成功")

    def crack(self):
        '''

        :return:
        '''
        self.open()
        button = self.get_touclick_button()
        button.click()
        time.sleep(1)
        # 打开获取验证码图片
        image = self.get_touclick_image()
        bytes_array = BytesIO()
        image.save(bytes_array,format="PNG")
        # 验证码识别
        result = self.CJY.PostPic(bytes_array.getvalue(),CJY_KIND)
        print(result)
        locations = self.get_points(result)
        self.touch_click_words(locations)
        self.touch_click_verify()
        # 判断是否登陆成功
        try:
            success = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,"btn write-btn","验证成功")))
            print(success)
        except:
            self.crack()

if __name__ =="__main__":
    crack = CracToucClick()
    crack.crack()