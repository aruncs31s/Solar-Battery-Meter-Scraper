"""
- Author : Arun CS
- 2024-09-24
"""

import time
from datetime import datetime

import requests as req

# Replace it with station ip addr
url = "http://172.16.32.8/data"

current_date = datetime.now().strftime("%Y-%m-%d")


def set_file(new_date):
    output_file = f"readings/normal/{new_date}_log.txt"
    output_file_csv = f"readings/csv/{new_date}_log.csv"
    get_reading(new_date, output_file, output_file_csv)


def get_reading(current_date, output_file, output_file_csv):
    try:
        with open(output_file_csv, "a") as f:
            f.write(f"Time,Battery Voltage\n")
        response = req.get(url)
        # Continuously read the data
        while True:
            # NOTE: This is a continues measurement so it should reset or save to new file every new day
            # TODO: Implement the above thing
            timestamp = datetime.now().strftime("%H:%M:%S")
            data_json = response.json()
            data = [
                data_json["battery_voltage"],
            ]
            with open(output_file, "a") as f:
                f.write(f"{timestamp},Battery Voltage{data[0]}\n")
            with open(output_file_csv, "a") as f:
                f.write(f"{timestamp},{data[0]}\n")
            #
            print(f"{timestamp} Battery Voltage {data[0]} \n")
            time.sleep(2)
            new_date = datetime.now().strftime("%Y-%m-%d")
            if current_date != new_date:
                set_file(new_date)
    except Exception as e:
        print(f"Error Getting Json {e}")
        time.sleep(10)
        current_date = datetime.now().strftime("%Y-%m-%d")
        set_file(current_date)


if __name__ == "__main__":
    set_file(current_date)
