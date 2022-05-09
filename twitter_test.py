from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
import time


PRO_UP = 150
PRO_DOWN = 10
TWITTER_EMAIL = 'YOUR EMAIL'
TWITTER_USER = 'YOUR TWITTER USERNAME'
TWITTER_PASSWORD = "YOUR TWITTER PASSWORD"

s = Service("YOUR CHROMEDRIVER FOLDER LOCATION")
driver = webdriver.Chrome(service=s)

''' CLASS to set up Twitter bot to assign webdriver path, also empty attributes to be updated.
'''
class InternetSpeedTwitterBot():
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)
        self.download = 0
        self.upload = 0
        self.ping = 0
        # self.get_internet_speed()

        
''' Function to connect to speedtest website:
  - locate elements to start test,
  - save element with speed attributes as variables to be printed out later in string format.
    '''
    def get_internet_speed(self):
        driver.get("https://www.speedtest.net/")
        button = driver.find_element(By.CSS_SELECTOR, ".start-button a")
        time.sleep(.25)
        button.click()

        time.sleep(60)
        # ping = driver.find_element(By.CLASS, ".ping-speed").text 
        self.ping = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        
        # download = driver.find_element(By.CLASS, ".download-speed").text
        self.download = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        # upload = driver.find_element(By.CSS_SELECTOR, ".upload-speed").text
        self.upload = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

        
        print(f"ping = {self.ping}")
        print(f"download = {self.download}")
        print(f"upload = {self.upload}")

''' Function that logins in Twitter to post results:
    - locates twitter login element to initiate login with username and password constants declared.
    - locates twitter text box element.
    - posts saved speed results.
    '''
    
    def tweet_at_provider(self):
        driver.get('https://twitter.com/login')
        time.sleep(10)

        login_twitter = driver.find_element(By.TAG_NAME,'input')
        login_twitter.send_keys(TWITTER_EMAIL)

        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div').click()

        time.sleep(5)
        user_twitter = driver.find_element(By.TAG_NAME, 'input')
        user_twitter.send_keys(TWITTER_USER)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/span/span').click()
        time.sleep(2)

        password_twitter = driver.find_element(By.NAME, "password")
        password_twitter.send_keys(TWITTER_PASSWORD)

        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]').click()

        time.sleep(5)
        tweet_text_box = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        tweet_text_box.click()
        time.sleep(2)                       
        tweet_text_box.send_keys(f"ATT is providing: {self.download} Download, {self.upload} Upload, and {self.ping} Ping!")
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div').click()

     
######## MAIN PROGRAM STARTS HERE: ########
bot = InternetSpeedTwitterBot(s)
bot.get_internet_speed()
bot.tweet_at_provider()
