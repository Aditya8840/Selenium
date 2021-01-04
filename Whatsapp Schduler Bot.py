import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def automation():
    contact = input('Enter Name or no. of contact exactly same as u save\n')
    text = input('Enter the message u want to send\n')
    driver = webdriver.Chrome('./driver/chromedriver')
    driver.get("https://web.whatsapp.com")
    print("Scan QR Code")
    time.sleep(15)
    print("Logged In")
    input_box_search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    input_box_search.click()
    time.sleep(2)
    input_box_search.send_keys(contact)
    time.sleep(2)
    selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
    selected_contact.click()
    input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    input_box.send_keys(text + Keys.ENTER)
    print('sucess')

#schedule.every().day.at("23:43").do(automation)
schedule.every().hours.do(automation)
while True:
    schedule.run_pending()
    time.sleep(1)
