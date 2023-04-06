import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# print(f"\n\n\n\n TITLE OF PAGE: {chrome_driver.title}\n\n\n")
def perform_task_using_driver(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    driver.maximize_window()
    driver.find_element('id','firstName').send_keys("Manav")
    driver.find_element(By.ID, "lastName").send_keys("Butani")
    driver.find_element(By.ID, "userEmail").send_keys("manav.butani@crestdatasys.com")
    driver.find_element(By.XPATH,"(//label[@for='gender-radio-1'])[1]").click()
    driver.find_element('id','userNumber').send_keys("9587525741")
    driver.find_element(By.ID,"dateOfBirthInput").send_keys(Keys.CONTROL,"a")
    driver.find_element(By.ID,"dateOfBirthInput").send_keys("10 Nov 2001",Keys.ENTER)
    driver.find_element(By.XPATH,'//*[@id="subjectsInput"]').send_keys("Python Training",Keys.ENTER)
    driver.find_element(By.XPATH,"(//label[normalize-space()='Sports'])[1]").click()
    driver.find_element(By.XPATH,"//input[@id='uploadPicture']").send_keys("C:/Users/manav.butani/Downloads/8.jpg")
    driver.find_element(By.XPATH,"//textarea[@id='currentAddress']").send_keys("Junagadh")
    driver.find_element(By.ID,"react-select-3-input").send_keys("Rajasthan",Keys.ENTER)
    driver.find_element(By.XPATH,'//*[@id="react-select-4-input"]').send_keys("Jaipur",Keys.ENTER)
    time.sleep(5)
    driver.find_element(By.ID,"submit").send_keys(Keys.ENTER)
    time.sleep(10)
    driver.close()
    # driver.quit()
    
if __name__ == "__main__":
        driver = webdriver.Chrome()
        driver.get('https://demoqa.com/automation-practice-form')
        perform_task_using_driver(driver)