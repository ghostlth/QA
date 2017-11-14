from selenium import webdriver
import time


def userCheck(userName,passWord):
    driver = webdriver.PhantomJS(executable_path='C:/Users\dell\Desktop\phantomjs-2.1.1-windows/bin/phantomjs')
    driver.get('http://172.88.1.200/login/Login.jsp?logintype=1')
    username = driver.find_element_by_xpath('//*[@id="loginid"]')
    password = driver.find_element_by_xpath('//*[@id="userpassword"]')
    button = driver.find_element_by_xpath('//*[@id="login"]')
    username.send_keys(userName)
    password.send_keys(passWord)
    # driver.get_screenshot_as_file('test.png')
    button.click()
    time.sleep(0.5)
    # 判断用户是否为OA用户
    try:
        driver.find_element_by_xpath('//*[@id="lfFoot"]/div[2]').click()
        print('成功')
        # driver.get_screenshot_as_file('test_success.png')
        return True
    except Exception as e:
        print(e)
        print('失败')
        # driver.get_screenshot_as_file('test_fail.png')
        return False
    finally:
        driver.close()

print(userCheck('lthui','Lthui42'))