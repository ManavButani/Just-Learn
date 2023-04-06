import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

def perform_task_using_driver(driver):
    driver.get('https://demoqa.com/login')
    driver.maximize_window()
    driver.find_element(By.XPATH,"//input[@id='userName']").send_keys("jadeja@gmail.com")
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Jadeja!123")
    # driver.implicitly_wait(4)
    
    driver.find_element(By.XPATH,"//button[@id='login']").click()
    time.sleep(4)