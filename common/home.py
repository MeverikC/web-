from Pms.src.common.driverCommon import drivercommon
from selenium.webdriver.common.by import By
import time

class home:
    def mjh_home(self):
        driver=drivercommon().getDriver('http://192.168.2.54:8080/Achievements-admin/login')
        driver.maximize_window()
        driver.find_element(By.XPATH,'//*[@id="signupForm"]/input[1]').send_keys('admin')
        driver.find_element(By.XPATH,'//*[@id="signupForm"]/input[2]').send_keys('admin123')
        driver.find_element(By.XPATH,'//*[@id="btnSubmit"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[3]/a/span[1]').click()
        driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[5]/a').click()
        driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[6]/a/span[1]').click()
        driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[8]/a/span[1]').click()
        driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[10]/a').click()
        now_url = driver.current_url
        print(now_url)
        if 'http://192.168.2.54:8080/Achievements-admin/index' == now_url:
            return True
        else:
            return False

    drivercommon().driver.close()