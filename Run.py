import time
from datetime import datetime
from main import check, driver


def main():
    while True:
        time.sleep(5)
        driver.refresh()
        check()
        time.sleep(25)
        print(datetime.now())

if __name__ == "__main__":
    main()