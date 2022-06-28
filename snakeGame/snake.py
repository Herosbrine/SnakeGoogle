#!/usr/bin/python3
from sqlite3 import Time, Timestamp
from selenium import webdriver
from time import sleep
from decouple import config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
import warnings
import time

###---------REMOVE THE DEPRECATIONWARNING---------###
warnings.filterwarnings("ignore", category=DeprecationWarning)


def FirstPhase(driver, Arrow, Timestamp):
    temp = 0
    while (1):
        if (int(driver.find_element_by_xpath("//*[@class='HIonyd']").text) > 0 and temp == 0):
            Arrow.send_keys(Keys.ARROW_DOWN)
            Timestamp = time.time()
            temp = 1
            break
    while (1):
        if (time.time() - Timestamp > 1):
            Arrow.send_keys(Keys.ARROW_LEFT)
            Timestamp = time.time()
            break
    while (1):
        if (time.time() - Timestamp > 1.4):
            Arrow.send_keys(Keys.ARROW_UP)
            Arrow.send_keys(Keys.ARROW_RIGHT)
            Timestamp = time.time()
            break
    return (Timestamp)

def GoTopRight(Arrow, Timestamp, TimeStampTurn):
    while (1):
        if (time.time() - Timestamp > 2):
            Arrow.send_keys(Keys.ARROW_UP)
            Arrow.send_keys(Keys.ARROW_RIGHT)
            Timestamp = time.time()
            return (Timestamp)
        if (time.time() - TimeStampTurn > 28.5):
            Arrow.send_keys(Keys.ARROW_DOWN)
            Timestamp = time.time()
            TimeStampTurn = time.time()
            return (Timestamp)

def GoTopLeft(Arrow, Timestamp, TimeStampTurn):
    while (1):
        if (time.time() - Timestamp > 2):
            Arrow.send_keys(Keys.ARROW_UP)
            Arrow.send_keys(Keys.ARROW_LEFT)
            Timestamp = time.time()
            return (Timestamp)
        if (time.time() - TimeStampTurn > 28.5):
            Arrow.send_keys(Keys.ARROW_DOWN)
            Timestamp = time.time()
            TimeStampTurn = time.time()
            return (Timestamp)

def GameLoop(Arrow, Timestamp):
    Temp = 0
    TimeStampTurn = time.time()
    while(1):
        if (Temp == 0):
            Timestamp = GoTopLeft(Arrow, Timestamp, TimeStampTurn)
            Temp = 1
        if (Temp == 1):
            Timestamp = GoTopRight(Arrow, Timestamp, TimeStampTurn)
            Temp = 0

def SnakeGame():
    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.google.com/search?q=jeu+snake&ei=iNC5Yv-SA42_lwSusJ74CQ&ved=0ahUKEwj_9r_x_M34AhWN34UKHS6YB58Q4dUDCBk&uact=5&oq=jeu+snake&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAELEDEEMyBAgAEEMyBQguEIAEMgUIABCABDIFCAAQgAQyBAgAEEMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgsIABCABBCxAxCDAToICAAQsQMQgwE6CAguELEDEIMBOgsILhCABBDHARCjAjoKCAAQsQMQgwEQQzoHCC4Q1AIQQzoECC4QQzoOCC4QgAQQsQMQgwEQ1AI6BwgAEIAEEApKBAhBGABKBAhGGABQAFiiCGCRCWgAcAF4AIABQIgBuwOSAQE5mAEAoAEBwAEB&sclient=gws-wiz")
    driver.set_page_load_timeout(30)
    driver.maximize_window()
    sleep(1)
    driver.find_elements_by_xpath("//*[@class='QS5gu sy4vM']")[0].click()
    sleep(2)
    driver.find_element_by_xpath("//*[@class='XlTvtc']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@class='FL0z2d Uxkl7b']").click()
    sleep(2)
    Arrow = driver.find_element_by_tag_name("input")
    try:
        Arrow.send_keys(Keys.ARROW_RIGHT)
    except:
        pass
    Timestamp = time.time()
    Timestamp = FirstPhase(driver, Arrow, Timestamp)
    GameLoop(Arrow, Timestamp)

    sleep(100)
def main():
    driver = SnakeGame()
main()