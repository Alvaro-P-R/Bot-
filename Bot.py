from selenium import  webdriver
from time import sleep
from selenium.common.exceptions import  ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

web = ("https://www.jesusninoc.com/powershell/page/2/")

driver = webdriver.Chrome()
driver.maximize_window()	
driver.get(web)	

a = 1

for i in range(100):
	web = f'https://www.jesusninoc.com/powershell/page/{a}'
	a +=1
	for z in range(20):
		
		
		driver.find_element_by_xpath('//*[@title="5 Stars"]').click()
		sleep(2)
	

	

	driver.get(web)
	


