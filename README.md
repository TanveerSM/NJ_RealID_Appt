This script can check if there are any available appointments for real id upgrades on the njmvc website. If there are any, it can ensure it is within the acceptable criteria (location, weekday, time) and fill the application, The user has to review the information, solve any captcha, and hit submit for the appt to be scheduled.


### Requirements
- Packages in the requirements.txt have to be installed, selenium is the essential one,
- Firefox webbrowser has to be installed, https://www.mozilla.org/en-US/firefox/
- geckodriver has to be available for your system, https://github.com/mozilla/geckodriver/releases


### Setup
- In the driver.py file, specify the location of the firefox and geckodriver executables,
- In the constants.py file, fill in the information that will be used to fill the appointment application form, and provide the acceptable dmv location, weekdays, time.


### Miscellaneous:
The script checks for available appts every 30 seconds, I recommend leaving it as is, however if you want to adjust it can be done in the run.py file at your own risk.
