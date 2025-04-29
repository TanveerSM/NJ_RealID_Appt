from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

def browser_config():
    #Browser config
    # Specifies the location of the firefox executable
    options = Options()
    binary = "C:\Program Files\Mozilla Firefox\Firefox.exe"
    options.binary_location = binary

    # specifies the location of geckodriver
    geckodriver = "E:\Downloads\geckodriver-v0.36.0-win64\geckodriver.exe"
    service = Service(executable_path=geckodriver)
    # configures and launches the firefox browser
    driver = webdriver.Firefox(options=options, service=service)
    return driver