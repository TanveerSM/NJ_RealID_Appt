import time
from datetime import datetime
from functions import check, driver

def main():
    while True:
        time.sleep(1)
        driver.refresh()
        result = check()
        if result == "found":
            print('\a')
            break
        time.sleep(29)
        print(datetime.now())

if __name__ == "__main__":
    main()