from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time, csv
from csv import writer
  

driver = webdriver.Chrome(executable_path='/var/local/learn/chromedriver')

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
      
        text = f'Namaskar {name} ji, %0a%0aWe have launched a full range of authorised healing crystals in very effective prices. You can have look at store here https://www.tatvascience.com/store. %0aLet us know if you have any query about healing crystals.%0a%0a Regards %0aTatvaScience.'

        numbers = ['917500101420','919501849601']

        for number in numbers:
            driver.get("https://web.whatsapp.com/send?phone="+number+"&text="+text)
            wait = WebDriverWait(driver, 600)
            
            
            x_arg = '//*[@id="side"]/header/div[1]/div/div'
            button = wait.until(EC.presence_of_element_located((
                By.XPATH, x_arg)))
            time.sleep(1)

            try:
                driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div[1]')
            except NoSuchElementException:
                button = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]/button')
                button.click()
                List=[name,number]
                writer_object = writer(updated_users)
                writer_object.writerow(List)

            time.sleep(1)
updated_users.close()