import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service



#Specifies the location of the firefox executable
options=Options()
binary="/usr/bin/firefox-esr"
options.binary_location=binary
# options.add_argument("--headless")


# Used this to get the snap version of firefox past the profile not found error, not needed with firefox-esr
# options.add_argument("-profile")
# options.add_argument("/home/tsm933/snap/firefox/common/.mozilla/firefox/i5pejxpx.default")

#specifies the location of geckodriver
geckodriver="/home/tsm933/Selenium Drivers/geckodriver"
service=Service(executable_path=geckodriver)

#confiures and launches the firefox browser
driver = webdriver.Firefox(options=options,service=service)

url : str = r"https://telegov.njportal.com/njmvc/AppointmentWizard/11/"

#goes to the url
driver.get(url)

acceptable_locations : str = ["Bayonne"]
second_location_name : str = "\nLicense Or Non Driver ID Renewal"

full_location_name = [acceptable_location + second_location_name for acceptable_location in acceptable_locations]
def check():
    grid = driver.find_element(By.ID,"locationsDiv")
    locations = grid.find_elements(By.CLASS_NAME,"locationCardContainer")
    for location in locations:
        if location.find_element(By.CSS_SELECTOR,"div[id^='dateText']").text != "No Appointments Available" and location.find_element(By.CLASS_NAME,"AppointcardHeader").text in full_location_name :
            location.find_element(By.CLASS_NAME,"btn-secondary").click()
            timeslot_grid = driver.find_elements(By.ID,"timeslots")
            for timeslot in timeslot_grid:
                button = timeslot.find_element(By.CLASS_NAME,"text-primary")
                link = button.get_attribute("href")
                driver.get(link)
                first_name_field = driver.find_element(By.ID,"firstName")
                first_name_field.clear()
                first_name_field.send_keys("Tanveer")
                last_name_field = driver.find_element(By.ID,"lastName")
                last_name_field.clear()
                last_name_field.send_keys("Mudhar")
                email_field = driver.find_element(By.ID,"email")
                email_field.clear()
                email_field.send_keys("TanveerSMudhar@gmail.com")
                phone_field = driver.find_element(By.ID,"phone")
                phone_field.clear()
                phone_field.send_keys("8482034288")
                license_field = driver.find_element(By.ID,"driverLicense")
                license_field.clear()
                license_field.send_keys("TestinginputInfo123212352")
                checkbox1 = driver.find_element(By.ID,"receiveTexts")
                checkbox1.click()
                checkbox2 = driver.find_element(By.CSS_SELECTOR,"input[name='Attest']")
                checkbox2.click()
                checkbox3 = driver.find_element(By.CSS_SELECTOR,"input[name='PtaAttest']")
                checkbox3.click()
            break
check()


# from slackclient import SlackClientdef slack_message(message, channel):
#     token = '[YOUR TOKEN]'
#     sc = SlackClient(token)    sc.api_call('chat.postMessage', channel=channel,
#                 text=message, username='My Sweet Bot',
#                 icon_emoji=':robot_face:')
