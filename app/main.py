from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.common.alert import Alert
import time, csv
from csv import writer

from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path='./../chromedriver')

updated_users = open('./../updated_users.csv', 'a')

with open('./../users.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if row[6] == 'NULL' or row[2] == 'NULL' or len(row[6]) > 10:
            continue
        name = row[2]
        number = row[6]
        if number[0] == '+':
            number = number[1:]
        if(len(number) == 10):
            number = '91'+number
      
        text = f'''Namaskar {name} ji, 
        %0a%0aTatva Science features a comprehensive selection of *Healing* *Crystals* at very affordable prices. Feel free to browse our store here:  https://www.tatvascience.com/store. 
        %0a%0a_Free_ _Services_:
        %0aCrystal Suggestions
        %0a1. according to your *Rashi*
        %0a2. according to *Common Problems*
        %0a3. to solve *Vastu*
        %0a4. according to *Tarot Cards*
        %0a%0aAccess all _free_ _services_ by clicking below link:
        %0a https://www.tatvascience.com
        %0a%0aLet us know if you have any query about healing crystals.
        %0a%0aRegards %0aTatvaScience.'''

        #%0aAccess all _free_ _services_ here: https://www.tatvascience.com
        #%0a%0a_Premium_ _Services_:
        #%0aCrystal Suggestions
        #%0a1. according to your *Birth* *chart* _(refundable 300/-)_. 
        #%0a2. according to your *specific* *problem*. _(refundable 100/-)_
        #%0a%0aAll kind of crystals available to be dispatched *same* *day*.

        driver.get("https://web.whatsapp.com/send?phone="+number+"&text="+text)

        # try:
        #     WebDriverWait(driver, 2).until (EC.alert_is_present())
        #     alert = driver.switch_to.alert
        #     alert.accept()
        # except TimeoutException:
        #     pass
        
        wait = WebDriverWait(driver, 20)
        x_arg = '//*[@id="side"]/header/div[1]/div/div'
        head = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        time.sleep(3)

        try:
            button = driver.find_element(By.CSS_SELECTOR, '#main > footer > div._2BU3P.tm2tP.copyable-area > div._1SEwr > div > div._3HQNh._1Ae7k > button')
            button.click()
            List=[name,number]
            writer_object = writer(updated_users)
            writer_object.writerow(List)
        except NoSuchElementException:
            continue

        time.sleep(15)
updated_users.close()
