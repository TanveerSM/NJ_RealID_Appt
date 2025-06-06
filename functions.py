from selenium.webdriver.common.by import By
from driver import browser_config
from datetime import datetime
import constants


driver = browser_config() #from driver.py

# goes to the url
driver.get(constants.url)
# this is the text below the name on the website
second_location_name: str = driver.find_element(By.CLASS_NAME, "AppointcardHeader").text.split("\n")[1]
# concats the second_location_name in the acceptable locations list
full_location_name = [acceptable_location + "\n" + second_location_name for acceptable_location in
                      constants.acceptable_locations]
def check():
    locations_grid = driver.find_element(By.ID, "locationsDiv")
    locations = locations_grid.find_elements(By.CLASS_NAME, "locationCardContainer")
    for location in locations:
        if location.find_element(By.CSS_SELECTOR, "div[id^='dateText']").text != "No Appointments Available":
            appt_date_1 = location.find_element(By.CSS_SELECTOR,"div[id^='dateText']").text.split("\n")[1].lstrip("Next Available: ")
            appt_date = datetime.strptime(appt_date_1,"%m/%d/%Y %I:%M %p") # "MM/DD/YYYY HH:MM AM"
            if\
            location.find_element(By.CLASS_NAME,"AppointcardHeader").text in full_location_name and\
            appt_date.year == constants.acceptable_year and\
            appt_date.month in constants.acceptable_month and\
            appt_date.weekday() in constants.acceptable_weekday and\
            appt_date.hour in constants.acceptable_hour:
                location.find_element(By.CLASS_NAME, "btn-secondary").click()
                timeslot_grid: list = driver.find_elements(By.ID, "timeslots")
                fill_form(timeslot_grid)
                print(appt_date)
                return "found"


def fill_form(timeslot_grid):
    for timeslot in timeslot_grid:
        button = timeslot.find_element(By.CLASS_NAME, "text-primary")
        link = button.get_attribute("href")
        driver.get(link)

        first_name_field = driver.find_element(By.ID, "firstName")
        first_name_field.clear()
        first_name_field.send_keys(constants.first_name)

        last_name_field = driver.find_element(By.ID, "lastName")
        last_name_field.clear()
        last_name_field.send_keys(constants.last_name)

        email_field = driver.find_element(By.ID, "email")
        email_field.clear()
        email_field.send_keys(constants.email)

        phone_field = driver.find_element(By.ID, "phone")
        phone_field.clear()
        phone_field.send_keys(constants.phone_no)

        license_field = driver.find_element(By.ID, "driverLicense")
        license_field.clear()
        license_field.send_keys(constants.licence_no)

        # opt in to text messages
        checkbox1 = driver.find_element(By.ID, "receiveTexts")
        checkbox1.click()
        # I am aware that after 30 minutes from making this appointment, I will NOT be able to change the personal information on this appointment. I will only be able to change the appointment date or time after 30 minutes
        checkbox2 = driver.find_element(By.CSS_SELECTOR, "input[name='Attest']")
        checkbox2.click()
        # read and agreed to the terms
        checkbox3 = driver.find_element(By.CSS_SELECTOR, "input[name='PtaAttest']")
        checkbox3.click()
        return
