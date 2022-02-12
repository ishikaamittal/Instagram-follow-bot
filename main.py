from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

path = Service("C:\chromedriver\chromedriver")
SIMILAR_ACCOUNT = "chefsteps"
USERNAME = ""
PASSWORD = ""


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.instagram.com/accounts/login/")

    def login(self):
        time.sleep(1)

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(1)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(6)
        self.driver.get("https://www.instagram.com/chefsteps/")
        time.sleep(2)
        followers = self.driver.find_element(By.TAG_NAME, "ul li a")
        followers.click()
        time.sleep(2)
        scroll = self.driver.find_element(By.CLASS_NAME, "isgrP")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH,
                                                         '/html/body/div[7]/div/div/div[2]/ul/div/li[1]/div/div[2]/button')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
