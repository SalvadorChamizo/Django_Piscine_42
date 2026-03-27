#!/usr/bin/python3

import sys
import antigravity


def geohashing(latitude, longitude, date, dow_jones_value):

    try:
        data = (date + "-" + dow_jones_value).encode()

        antigravity.geohash(float(latitude), float(longitude), data)
    except Exception:
        print("Error")


if __name__ == '__main__':
    if (len(sys.argv) != 5):
        print("Error: Invalid number of arguments. Expected: geohashing.py <latitude> <longitude> <date> <dow_jones_value>")

    geohashing(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
# python3 geohashing.py 50.468964 30.462287 2019-11-07-27590.16
# python3 geohashing.py 37.421542 -122.085589 2005-05-26-10458.68