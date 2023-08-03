from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import urllib
import requests

def get_contactinfo(driver,target):
    wait=WebDriverWait(driver,100)
    driver.get("https://web.whatsapp.com/")

    # search='//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p'
    # search_p=wait.until(EC.presence_of_element_located((By.XPATH,search)))
    # search_p.click()


    contact_path='//span[contains(@title,'+ target +')]'
    contact=wait.until(EC.presence_of_element_located((By.XPATH,contact_path)))
    contact.click()
    
    
    try:
        information_pane='//*[@id="main"]/header/div[2]/div/div/span'
        about_box=wait.until(EC.presence_of_element_located((By.XPATH,information_pane)))
        about_box.click()
    except Exception as e:
        print(e)

    try:
        name ='//*[@id="main"]/header/div[2]/div[1]/div/span'      #'//*[@id="app"]/div/div/div[6]/span/div/span/div/div/section/div[1]/div[2]/h2/span' #'//span[@data-testid="contact-info-subtitle"]'
        contact_name = driver.find_element(By.XPATH, name)
        print("name:",contact_name.text)
        time.sleep(5)
    except:
        print("name: No name given to this number")
    try:
        number = '//span[@class="enbbiyaj e1gr2w1z hp667wtd"]'
        contact_number = driver.find_element(By.XPATH, number)
        print("Phone_Number:",contact_number.text)
    except Exception as e:
        print(e)
    try:
        preview_img =  '/html/body/div[1]/div/div/div[6]/span/div/span/div/div/section/div[1]/div[1]/div/img'
        previewImageElement = driver.find_element(By.XPATH,preview_img)
        previewImageURL = previewImageElement.get_attribute("src")
        print("profile_pic", previewImageURL)
    except:
        print("Profil pic:no image")

    try:
        about = '/html/body/div[1]/div/div/div[6]/span/div/span/div/div/section/div[2]/span/span'
        status = driver.find_element(By.XPATH, about)
        print("Status:",status.text)
    except:
        print("Status:no status")

    try:

        last_seen = '//*[@id="main"]/header/div[2]/div[2]/span'
        seen = driver.find_element(By.XPATH, last_seen)
        print("last_seen:", seen.text)
    except:
        print("last_seen:last seen is hiddens")

target_contacts = ['"Aeb"','"Cc"' '"Bab"']
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))

for target in target_contacts:
    get_contactinfo(driver, target)
    time.sleep(100) 


