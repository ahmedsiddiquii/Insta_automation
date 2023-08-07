import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

# driver.get("https://www.instagram.com/")
# time.sleep(5)  
df = pd.read_csv('Probate_Sample.csv')

names = df['id']
print(names)
passwords = df['Password']
print(passwords)
search1 =df['username']
print(search1)
links= df['links']
print(links)

driver.get("https://www.instagram.com/")
time.sleep(5)  
login_insta = driver.find_element(by='xpath',value=  '//input[@aria-label="Phone number, username, or email"]').send_keys(names)
password= driver.find_element(by='xpath',value='//input[@type="password"]').send_keys(passwords)
time.sleep(5)
login= driver.find_element(by='xpath', value='//div//button[@class="_acan _acap _acas _aj1-"]').click()
time.sleep(10)


def single_person():
    for searches in search1:
        driver.get(f"https://www.instagram.com/{searches}/")
        time.sleep(5)
        try:
            send_message_button = driver.find_element(by='xpath', value='//div[contains(text(), "Message")]')
            send_message_button.click()        
            time.sleep(10)
            message_input= driver.find_element(by='xpath',value='//p[@class="xat24cr xdj266r"]')
            message_input.send_keys("hello")
            message_input.send_keys(Keys.ENTER)
        except:
            pass
        
single_person()

def send_messages_to_top_30_users():
    try:
        for name, password in zip(names, passwords):
            driver.get("https://www.instagram.com/")
            time.sleep(5) 
            login_insta = driver.find_element(by='xpath',value=  '//input[@aria-label="Phone number, username, or email"]').send_keys(name)
            password= driver.find_element(by='xpath',value='//input[@type="password"]').send_keys(password)
            time.sleep(5)
            login= driver.find_element(by='xpath', value='//div//button[@class="_acan _acap _acas _aj1-"]').click()
            time.sleep(15)
    except:
        pass
    for link in links:
        driver.get(link)
        time.sleep(5)
        likes_button = driver.find_element(by='xpath',value='//span[@class="x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"]')
        likes_button.click()
        time.sleep(5)
        temp = []
        likes_popup = driver.find_elements(by='xpath', value='//div[@class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x6ikm8r x10wlt62 x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"]//a')
        for i in range(min(60, len(likes_popup))):
            link = likes_popup[i].get_attribute("href")
            temp.append(link)
            if len(set(temp)) >= 30:
                break
        unique_temp = list(set(temp))
        for link in unique_temp:
            print(link)
    for link in unique_temp:
        driver.get(link)
        time.sleep(5)
        
        try:
            send_message_button = driver.find_element(by='xpath', value='//div[contains(text(), "Message")]')
            send_message_button.click()
            time.sleep(10)
            message_input= driver.find_element(by='xpath',value='//p[@class="xat24cr xdj266r"]')
            message_input.send_keys("hello")
            time.sleep(2)
            message_input.send_keys(Keys.ENTER)
        except:
            pass
send_messages_to_top_30_users()
        
        
        