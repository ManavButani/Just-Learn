"""Read the table content from here and print them in console."""

from selenium import webdriver
from selenium.webdriver.common.by import By
def main():
    chrome=webdriver.Chrome()
    chrome.get('https://www.w3schools.com/html/html_tables.asp')
    chrome.implicitly_wait(5)
    table=chrome.find_element(By.XPATH,'//*[@id="customers"]')
    heading_1=chrome.find_element(By.XPATH,'//*[@id="customers"]/tbody/tr[1]/th[1]')
    heading_2=chrome.find_element(By.XPATH,'//*[@id="customers"]/tbody/tr[1]/th[2]')
    heading_3=chrome.find_element(By.XPATH,'//*[@id="customers"]/tbody/tr[1]/th[3]')
    with open("manav.txt","a+") as f:
        f.write(f"{heading_1.text}        {heading_2.text}        {heading_3.text}")
    for row in table.find_elements(By.CSS_SELECTOR,'tr'):
        for cell in row.find_elements(By.CSS_SELECTOR,'td'):
            with open("manav.txt","a+") as f:
                f.write(f"{cell.text}  " )
        with open("manav.txt","a+") as f:
                f.write("\n")
        
if __name__=="__main__":
    main()