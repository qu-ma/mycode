#!/usr/bin/python3

import requests
import time

API = "http://api.open-notify.org/iss-now.json"

def main():
    resp = requests.get(API).json()
    # print(resp)

    time_stamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(resp['timestamp']))
    latitude = resp['iss_position']['latitude']
    longitude = resp['iss_position']['longitude']

    print("CURRENT LOCATION OF THE ISS:")
    print(f"Timestamp: {time_stamp}\nLATITUDE: {latitude}\nLOGITUDE: {longitude}")

if __name__ == "__main__":
    main()
