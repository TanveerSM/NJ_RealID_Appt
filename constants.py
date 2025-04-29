first_name :str = "Johnny"
last_name :str = "Doe"
phone_no :int = "123456789"
email :str = "email@gmail.com"
licence_no :str = "X11112222233333"
# url that the browser will start from
url : str = r"https://telegov.njportal.com/njmvc/AppointmentWizard/12/"
#acceptable location, case sensitive
# specify which dmv location you are willing to go to
acceptable_locations: str = ["Eatontown", "Edison", "Freehold", "Rahway", "South Plainfield"]
acceptable_year :int = 2025
acceptable_month :list = [4,5,6]
acceptable_weekday :list = [0,1,2,3,4,5,6] #Monday 0, Sunday 6
acceptable_hour :list = [8,9,10,11,12,13,14,15,16] #hour in 24H format
