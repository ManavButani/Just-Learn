"""
1. Write a program that
○ Open Chrome & Firefox browsers one after the other and perform all the given actions
○ Resize the window
○ maximize the window
○ Hit the URL: http://www.google.com
○ Print the title of the tab
○ Open a new tab
○ Hit the URL: https://stackoverflow.com
○ Print the title of the tab
○ Close the first window
○ Close the session

"""
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options

def perform_task_using_driver(driver):
    """Performing task like open window,close window and open multiple tabs using driver.
    Args:
        driver ([webdriver]): Chrome or Firefox Driver
    """
    # minimize the window
    driver.set_window_size(700, 700)
    time.sleep(1)
    # maximize the window
    driver.maximize_window()
    time.sleep(1)
    # open first tab
    driver.get("http://www.google.com")
    time.sleep(1)
    print(driver.title)
    # second tab
    driver.execute_script("window.open('about:blank', 'tab2');")
    driver.switch_to.window("tab2")
    driver.get("https://stackoverflow.com")
    time.sleep(1)
    print(driver.title)
    # switch to first tab
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    # closed the first tab
    driver.close()
    # close the session
    time.sleep(1)
    driver.quit()
    
def main():
    """
    Function will configure the driver and call another function.
    """
    try:
        chrome_driver = webdriver.Chrome("chromedriver.exe")
        perform_task_using_driver(chrome_driver)
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        firefox_driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe', options=options)
        perform_task_using_driver(firefox_driver)
    except Exception as e:
        print(f"------- \n {e} \n --------------")

if __name__ == "__main__":
    main()
