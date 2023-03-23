from selenium import webdriver
import time

first_name = "Ilia"
last_name = "Bogatyrev"
username = "ilias.sbogatyrev"
password = "MyPassword123"
phone = '+37258222211'
birthday_month = "Febraury"
birthday_day = "4"
birthday_year = "1991"

browser = webdriver.Chrome()
browser.get("https://accounts.google.com/signup")

browser.find_element('name', "firstName").send_keys(first_name)
browser.find_element('name', "lastName").send_keys(last_name)
browser.find_element('name', "Username").send_keys(username)
browser.find_element('name', "Passwd").send_keys(password)
browser.find_element('name', "ConfirmPasswd").send_keys(password)

browser.find_element('id', "accountDetailsNext").click()
time.sleep(3)

browser.find_element('id','phoneNumberId').send_keys(phone)
time.sleep(3)
browser.find_element('xpath', '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()

time.sleep(3)
browser.find_element('name', "day").send_keys(birthday_day)
browser.find_element('name', "year").send_keys(birthday_year)
browser.find_element('name', "month").send_keys(birthday_month)

browser.find_element('name', "personalDetailsNext").click()
time.sleep(2)

browser.find_element('name', "termsofserviceNext").click()

assert "Google Account" in browser.title

time.sleep(10)
browser.quit()
