# 设置为开发者模式，防止被各大网站识别出来使用了Selenium console中输入window.navigator.webdriver 测试
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