import unittest
from selenium import webdriver
import time

class TestOne(unittest.TestCase):

	def setUp(self):
		self.startTime = time.time()
		#self.driver = webdriver.PhantomJS()
		options = webdriver.ChromeOptions()
		options.add_argument("headless")
		self.driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=options)

		self.driver.set_window_size(1120,550)

	def test_url(self):
		self.driver.get("http://duckduckgo.com")
		self.driver.find_element_by_id("search_form_input_homepage").send_keys("realpython")
		self.driver.find_element_by_id("search_button_homepage").click()
		self.assertIn("https://duckduckgo.com/?q=realpython",self.driver.current_url)

	def tearDown(self):
		t = time.time() - self.startTime
		print("%s: %.3f" %(self.id(),t))
		self.driver.quit()

class TestTwo(unittest.TestCase):

	def setUp(self):
		self.startTime = time.time()
		options = webdriver.ChromeOptions()
		options.add_argument("headless")
		self.driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=options)
#		self.driver = webdriver.PhantomJS()
#		self.driver.set_window_size(1120,550)

	def test_url(self):
		time.sleep(2)
		self.driver.get("https://app.simplegoods.co/i/IQCZADOY")
		button = self.driver.find_element_by_id("payment-amount").get_attribute("value")
		#self.assertEqual(u'Pay - $60.00',button)
		self.assertEqual(u'60.00',button)

	def tearDown(self):
		t = time.time() - self.startTime
		print("%s: %.3f" %(self.id(),t))
		self.driver.quit()
		

if __name__=='__main__':
	unittest.main()