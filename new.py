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
import requests

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


# def single_person():
#     for searches in search1:
#         driver.get(f"https://www.instagram.com/{searches}/")
#         time.sleep(5)
#         try:
#             send_message_button = driver.find_element(by='xpath', value='//div[contains(text(), "Message")]')
#             send_message_button.click()        
#             time.sleep(10)
#             message_input= driver.find_element(by='xpath',value='//p[@class="xat24cr xdj266r"]')
#             message_input.send_keys("hello")
#             message_input.send_keys(Keys.ENTER)
#         except:
#             pass
        
# single_person()

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
    likes_button = driver.find_element(by='xpath',value='//span[@class="x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"]')
    likes_button.click()
    time.sleep(5)

    likes1 = driver.find_element(by='xpath', value='//div[@style="height: 356px; overflow: hidden auto;"]')

    # Desired number of links to collect
    target_links_count = 30
    action =ActionChains(driver)
    

    while True:
        # Scroll within the likes1 element using JavaScript
        scroll_script = "arguments[0].scrollBy(0, arguments[0].scrollHeight);"
        # driver.execute_script(scroll_script, likes1)
        # action.send_keys(likes1,Keys.DOWN)
        action.move_to_element(likes1).send_keys(Keys.DOWN).perform()
        
        time.sleep(2)  # You can adjust this delay as needed
        
        likes_popup = likes1.find_elements(by='xpath', value='.//a')
        collected_links = [link.get_attribute("href") for link in likes_popup]
        unique_links = list(set(collected_links))
        
        if len(unique_links) >= target_links_count:
            break

    for link in unique_links:
        print(link)

    for link in unique_links:
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
        
        
        