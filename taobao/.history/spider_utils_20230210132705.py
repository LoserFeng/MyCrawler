
import random
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import logging


MONITOR_FLAG=False



def get_browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation','enable-logging'])
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--ignore-certificate-errors')   #主要是该条
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=options)
    # 使用js关闭检测机制
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
                        Object.defineProperty(navigator, 'webdriver', {
                          get: () => undefined
                        })
                      """
    })
    return driver



def login(driver,login_id, login_password):
    driver.get('https://login.taobao.com/')
    print('title is ', driver.title)
    # if driver.title=='验证码拦截':
    #     slider(url)

    # 发送命令-查找元素与操作元素
    # 找到输入账号框，清除框内信息，再输入你的账号
    driver.find_element(By.CSS_SELECTOR, '#fm-login-id').clear()
    driver.find_element(By.CSS_SELECTOR, '#fm-login-id').send_keys(login_id)
    # 找到输入密码框，清除框内信息，再输入你的密码
    driver.find_element(By.CSS_SELECTOR, '#fm-login-password').clear()
    driver.find_element(By.CSS_SELECTOR, '#fm-login-password').send_keys(login_password + Keys.ENTER)




def slider(url,driver):
    print(driver.title, url)
    # if driver.title == '验证码拦截':
    #     print(driver.title, url)
    #     time.sleep(random.randint(3, 5))  # 随机休眠5-10s
    #     try:
    #         if driver.find_element(By.CSS_SELECTOR, "#\`nc_1_refresh1\`").is_displayed():
    #             driver.find_element(By.CSS_SELECTOR, "#\`nc_1_refresh1\`").click()
    #             time.sleep(random.randint(1, 3))
    #             slider = driver.find_element(By.CSS_SELECTOR, '#nc_1_n1z')
    #
    #     except:
    #         slider = driver.find_element(By.CSS_SELECTOR, '#nc_1_n1z')
    #         pass

    slider = driver.find_element(By.CSS_SELECTOR, '#nc_1_n1z')
    # 拖拽滑块
    action = ActionChains(driver)
    action.click_and_hold(slider)
    sum = 0
    while True:
        x = random.randint(5, 70)
        action.move_by_offset(x, 0)
        time.sleep((random.randint(1, 2)) / 10)
        sum += x
        if sum >= 260:
            break
    time.sleep(1)
    action.release().perform()
    time.sleep(1)



def verify(driver):
    cnt=0

    while driver.title == '验证码拦截':
        cnt +=1
        logging.info(f'正在尝试第{str(cnt)}次')
        time.sleep(random.randint(2, 3))
        slider('logining',driver)
        if cnt<=30:
            # 打开新标签页并切换到新标签页
            driver.refresh()
            # driver.switch_to.new_window('tab')
        else:
            print('重复尝试多次失败，程序暂停')
            return False

        time.sleep(random.randint(3, 5))
    return True



def monitor(driver):
    # logging.basicConfig(level=logging.DEBUG,
    #                 filename='./log.txt',
    #                 filemode='a',
    #                 format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    global MONITOR_FLAG
    MONITOR_FLAG=True
    logging.info('开启monitor')
    while(MONITOR_FLAG):
        logging.info('monitor正在工作')
        time.sleep(3)
        if driver.title=='验证码拦截':
            logging.info('遇到拦截')
            flag=verify(driver)
            if not flag:
                logging.info('重复尝试多次失败，正在退出')
                driver.quit()
                return -1
    logging.info('monitor终止')
    return 0




def stop_monitor():
    MONITOR_FLAG=False
    time.sleep(6)