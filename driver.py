from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

def browser_config():
    #Browser config
    # Specifies the location of the firefox executable
    options = Options()
    binary = "/usr/bin/firefox-esr"
    options.binary_location = binary

    # specifies the location of geckodriver
    geckodriver = "/home/XXXX/Selenium Drivers/geckodriver"
    service = Service(executable_path=geckodriver)
    # configures and launches the firefox browser
    driver = webdriver.Firefox(options=options, service=service)
    return driver
