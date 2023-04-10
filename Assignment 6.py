from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Initialize the webdriver
driver = webdriver.Chrome()

# Navigate to the URL of the form
driver.get("https://automationexplore.com/selenium-automation-practice-page/")

# Fill in the first name field
first_name_field = driver.find_element(By.ID, "firstname")
first_name_field.send_keys("Ilia")

# Fill in the last name field
last_name_field = driver.find_element(By.ID, "lastname")
last_name_field.send_keys("Bog")

# Fill in the email field
email_field = driver.find_element(By.ID, "email")
email_field.send_keys("ilia.bogatyrev@ut.ee")

# Select gender
gender_male = driver.find_element(By.XPATH, "//input[@value='male']")
gender_male.click()

# Select checkboxes
student_checkbox = driver.find_element(By.XPATH, "//input[@name='Student']")
student_checkbox.click()

working_checkbox = driver.find_element(By.XPATH, "//input[@name='working']")
working_checkbox.click()

# Select a country from the drop-down list
country_dropdown = Select(driver.find_element(By.NAME, "country"))
country_dropdown.select_by_value("UAE")

# Select multiple skills from the multi-select drop-down list
skills_dropdown = Select(driver.find_element(By.ID, "skillsmultiple"))
skills_dropdown.select_by_value("MT")
skills_dropdown.select_by_value("AT")

# Click the "Click Me!" button
click_me_button = driver.find_element(By.ID, "simplebutton")
click_me_button.click()

# Click the "Click here to get Alert" button and accept the alert
alert_button = driver.find_element(By.ID, "alertbutton")
alert_button.click()
alert = driver.switch_to.alert
alert.accept()

# Close the browser window
driver.quit()