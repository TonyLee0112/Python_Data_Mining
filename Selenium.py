from selenium import webdriver
import time

# driver = webdriver.Edge()
# driver = webdriver.Chrome()
# url = "https://sophiagreen.co.kr/member/login"
# url = "https://nid.naver.com/nidlogin.login"

driver.get(url)

# time.sleep(0.5)

driver.find_element(by='name', value='id').send_keys('shb06129')
time.sleep(2)
driver.find_element(by='name', value='pw').send_keys('leesh970927!')
