from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://timemachine1-vm.berea.edu/ultratime/ultrapunch/login.aspx')

myID = driver.find_element_by_xpath('//*[@id="UserID"]')
myID.send_keys('00725946')

myPassword = driver.find_element_by_xpath('//*[@id="UserPass"]')
myPassword.send_keys('1234')

inButton = driver.find_element_by_xpath('//*[@id="BUTIN"]')
inButton.click()
