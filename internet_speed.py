# internet_speed.py
# https://pythonprogramming.org/monitor-your-internet-with-python/

import speedtest
import datetime
import time
import csv

s = speedtest.Speedtest()

with open("internet_speed.csv", mode="w") as speedcsv:
    dictfields = ['time', 'downspeed', 'upspeed']
    csv_writer = csv.DictWriter(speedcsv, fieldnames=dictfields)
    csv_writer.writeheader()
    while True:
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        downspeed = round(round(s.download()) / (1024 * 1024), 2)
        upspeed = round(round(s.upload()) / (1024 * 1024), 2)
        print(f"time: {time_now}, download speed: {downspeed} Mb/s, upload speed: {upspeed} Mb/s")
        csv_writer.writerow({
            "time": time_now,
            "downspeed": downspeed,
            "upspeed": upspeed
        })
        # Pause for 2 minutes
        time.sleep(2 * 60)