from selenium import webdriver
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element_value

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
button = browser.find_element_by_id("book")
button.click()

browser.execute_script("window.scrollBy(0, 150)", "")

import math
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
browser.find_element_by_id('answer').send_keys(str(math.log(abs(12*math.sin(int(x))))))

button1 = browser.find_element_by_id("solve")
button1.click()


time.sleep(5)
browser.quit()
