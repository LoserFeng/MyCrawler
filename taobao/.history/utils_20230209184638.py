# 设置为开发者模式，防止被各大网站识别出来使用了Selenium console中输入window.navigator.webdriver 测试

from selenium import webdriver

def get_browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
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
