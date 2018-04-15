# coding:utf-8
import time
from selenium import webdriver


class LoginPage():
    '''登录页面'''

    def __init__(self, driver):
        self.driver = driver   # 形参
        self.driver.get("http://127.0.0.1/zentao/user-login.html")

    def logout(self):
        '''登出'''
        # driver = webdriver.Firefox()
        self.driver.delete_all_cookies() # 删除所有的cookies
        self.driver.refresh()

    def input_username(self,usrname):
        '''输入账号'''
        self.driver.find_element_by_id("account").send_keys(usrname)

    def input_psw(self,psw):
        '''输入密码'''
        self.driver.find_element_by_name("password").send_keys(psw)

    def click_login_button(self):
        '''点击登录按钮'''
        self.driver.find_element_by_id("submit").click()

    def login(self,username="admin",psw="123456"):
        '''登录流程:三步'''
        self.input_username(username)
        self.input_psw(psw)
        self.click_login_button()

    def get_login_result(self):
        '''获取登录的结果'''
        try:
            t = self.driver.find_element_by_css_selector("#userMenu>a").text
            return t
        except:
            print("登录失败！！！，返回空字符")
            return ""


if __name__ == "__main__":
    driver = webdriver.Firefox()
    loginpage = LoginPage(driver)
    res = loginpage.login()
    print(res)
    # 断言
    loginpage.logout()

