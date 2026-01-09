from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
from pynput.keyboard import Key, Controller
driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
time.sleep(5)
email_input = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[1]/div/label/input')
email_input.send_keys('ab.dullah097')
password_input = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[2]/div/label/input')
password_input.send_keys('@Galino8a')

time.sleep(2)
login_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[3]/button/div')
login_button.click()
time.sleep(5)

try:
    savenow_button = driver.find_element(
        By.XPATH,
        '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/section/div/button'
    )
    savenow_button.click()
except NoSuchElementException:
    print("Save Now button not found on the page.")
except ElementClickInterceptedException:
    print("Save Now button was found but could not be clicked (covered or not interactable).")
except Exception as e:
    print(f"Unexpected error while clicking Save Now button: {e}")
time.sleep(5)
newpost_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[7]/div/span/div/a/div')
newpost_button.click()
time.sleep(8)
addpost_button = driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/button')
addpost_button.click()
time.sleep(6)
keyboard = Controller()
keyboard.type("C:\\Users\\HP\\Desktop\\django\\36c8e3b6-01e2-434e-93ec-fb622333134d.png")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(5)

NEXT1 = driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div').click()
time.sleep(2)
NEXT2 = driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div').click()
time.sleep(4)
DESCRIPTION = driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div[1]/p').send_keys("autmoated post")
time.sleep(2)
SHARE = driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div').click()
time.sleep(1000)


# /html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div   next 1
# /html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div    next 2
# /html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div    share button