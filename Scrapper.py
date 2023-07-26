from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
import pywhatkit
import time
import pyautogui
import keyboard as k
import undetected_chromedriver as uc
import os
import wave
from pygame import mixer


@dataclass
class Product:
    name: str = None


def print_natiga(url, Username,password):
    try:

        counter = 0
        options = Options()
        print("1")

        options.add_argument('--disable-gpu')
        print("3")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        print("4")
        driver.get(url)

        counter = 0
        driver.find_element_("xpath",
                            '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/input').send_keys(
            Username)
        print(Username)
        time.sleep(2)
        driver.find_element("xpath",
                            '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/div[2]/div/input').send_keys(
            password)
        print(password)
        time.sleep(2)
        driver.find_element("xpath",
                            '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]').click()

        driver.find_element("xpath",
                            '/html/body/div/div[1]/div[1]/div/div/div[1]').click()

        try:
            name = driver.find_element("xpath",
                                       '/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div/section/div[2]/div[1]/div[2]/div[1]/div').text
        except:
            name = "None"
            pass
        driver.quit()
        return Product(name=name)
    except:
        name = "None"

    return Product(name=name)


if __name__ == '__main__':

    clickty = True
    while clickty:

        x = print_natiga("https://discord.com/login", 'username','pass')

        if "None" not in x.name:
            clickty = False
            time.sleep(1)
        else:
            print("Not yet")
            time.sleep(30)