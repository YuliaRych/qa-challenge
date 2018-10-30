from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://www.google.com")

wait = WebDriverWait(driver, 10)

search = "input[name='q']"
inputFieldq = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,search)))
inputFieldq.send_keys("test automation is awesome")
inputFieldq.submit()

title = driver.title
print('Title is: ' + title)

driver.quit()