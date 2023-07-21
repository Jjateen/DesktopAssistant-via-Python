import os
from time import sleep
import config

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.headless = True  # if false all the stuff will load in backend
# Driver path cheak your current browser first than download respectively >>
# chrome://settings/help

url = 'https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F'


def login(Email, Password):

    global driver,wait
    driver = webdriver.Chrome('C:\PythonX\Python_Exp_yt\Spotify Automation\chromedriver.exe')
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get(url)

    driver.find_element(By.CSS_SELECTOR, "#login-username").send_keys(Email)
    driver.find_element(By.CSS_SELECTOR, "#login-password").send_keys(Password)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='login-button'] div:nth-child(1)"))).click()


# spotdl https://open.spotify.com/track/0VjIjW4GlUZAMYd2vXMi3b

def download():
    str1 = "spotdl "
    str2 = driver.current_url
    str = str1 + str2
    os.system(str)
    print("downloading")

def like_song():
    driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div/button[1]').click()
    print("liked the song")

def playlist():
    driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div/button[2]').click()

    # Hover to playlist
    sub_menu = driver.find_element(By.XPATH, "//span[normalize-space()='Add to playlist']")
    chain = ActionChains(driver)
    chain.move_to_element(sub_menu).perform()

    # Add song in anime_song playlist

    wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@role='menuitem']//span[@dir='auto'][normalize-space()='anime song']"))).click()