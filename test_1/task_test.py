from selenium import webdriver
from selenium.webdriver import ActionChains

dr = webdriver.Chrome(executable_path="/home/paul/workspace/homework_automation/chromedriver")
dr.implicitly_wait(7)
dr.get("https://demo.oxwall.com/")
login = dr.find_element_by_id("loginAsAdmin")
login.click()

login_input = dr.find_element_by_xpath('//*[@name="identity"]')
password_input = dr.find_element_by_xpath('//*[@name="password"]')
submit_bttn = dr.find_element_by_name("submit")

login_input.click()
#login_input.send_keys("admin")
password_input.click()
#password_input.send_keys("pass")
submit_bttn.click()
header_bttn = dr.find_element_by_class_name('ow_console_dropdown_hover')
cursor = ActionChains(dr)
cursor.move_to_element(header_bttn).pause(1).perform()
logout_bttn = dr.find_element_by_link_text("Sign Out")
logout_bttn.click()

dr.quit()