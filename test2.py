from appium import webdriver


class a :
    def b(self,PC_ip="127.0.0.1",PC_port="4723"):
        PC = 'http://' + PC_ip + ':' + PC_port + '/wd/hub'
        print(PC)

a().b()

desired_caps = {
    'platformName': "Android",
    'platformVersion': "9",
    'deviceName': '7&1c3e0558&0&0001',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,
    'appPackage': "com.tencent.mm",
    'appActivity': "com.tencent.mm.ui.LauncherUI",
    'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'
                      }
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)