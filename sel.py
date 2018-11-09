from selenium import webdriver
#driver = webdriver.PhantomJS()
#driver.set_window_size(1120,550)

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)

driver.get("https://duckduckgo.com")
driver.find_element_by_id("search_form_input_homepage").send_keys("realpython")
driver.find_element_by_id("search_button_homepage").click()
print (driver.current_url)
driver.quit