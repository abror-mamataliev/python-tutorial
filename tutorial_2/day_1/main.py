from datetime import datetime
from tkinter import (
    Button,
    Frame,
    Label,
    Tk,
)

from requests import get

# root = Tk()
# root.title("Weather app: Day 1")
# root.resizable(False, False)
#
# frame = Frame(root)
# frame.pack()

response = get("https://ipinfo.io/loc")
if response.status_code != 200:
    print("Failed to get location")
    exit(1)
lat, lon = response.text.split(",")

today = datetime.now()

response = get(
    "https://api.openweathermap.org/data/3.0/onecall",
    params={
        'lat': lat,
        'lon': lon,
        # 'date': today.strftime("%Y-%m-%d"),
        'exclude': 'current,minutely,daily,alerts',
        'appid': "e54abbee525c90e62c1587e6d90a6407"
    }
)
# response = get(
#     "https://api.openweathermap.org/data/2.5/forecast/daily",
#     params={
#         'lat': lat,
#         'lon': lon,
#         # 'date': today.strftime("%Y-%m-%d"),
#         'cnt': 10,
#         'appid': "e54abbee525c90e62c1587e6d90a6407"
#     }
# )
print(response.json())
