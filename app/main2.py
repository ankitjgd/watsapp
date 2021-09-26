from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time, csv
from csv import writer

from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path='./../chromedriver')

updated_users = open('./../updated_users2.csv', 'a')
counter = 0
with open('./../users.csv') as csv_file:
    csv_reader = reversed(list(csv.reader(csv_file, delimiter=';')))
    line_count = 0
    for row in csv_reader:
        if counter > 100:
            exit(0)
        if row[6] == 'NULL' or row[2] == 'NULL' or len(row[6]) > 10:
            continue
        name = row[2]
        number = row[6]
        if number[0] == '+':
            number = number[1:]
        if(len(number) == 10):
            number = '91'+number
      
        text = f'''Namaskar {name} ji, 
        %0a%0a*Healing* *Crystals* now at your doorsteps in very affordable prices. Feel free to browse our store here:  https://www.tatvascience.com/store. 
        %0a%0aOur _Free_ _Services_:
        %0aCrystal Suggestions
        %0a1. For *Couples*.
        %0a2. According to your *Rashi*
        %0a3. According to *Common Problems*
        %0a4. To solve *Vastu*
        %0a5. According to *Tarot Cards*
        %0a%0aAccess all _free_ _services_ by clicking below link:
        %0a https://www.tatvascience.com
        %0a%0aWant to go for personised service, book appointment below.
        %0ahttps://www.tatvascience.com/online-appointment
        %0a%0aRegards %0aTatvaScience.'''
        #%0a%0aLet us know if you have any query about healing crystals.
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
        
        wait = WebDriverWait(driver, 40)
        x_arg = '//*[@id="side"]/header/div[1]/div/div'
        head = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        time.sleep(10)

        try:
            button = driver.find_element(By.CSS_SELECTOR, '#main > footer > div._2BU3P.tm2tP.copyable-area > div > div > div._2lMWa > div._3HQNh._1Ae7k > button')
            button.click()
            List=[name,number]
            writer_object = writer(updated_users)
            writer_object.writerow(List)
            counter = counter + 1
        except NoSuchElementException:
            continue

        time.sleep(15)
updated_users.close()
