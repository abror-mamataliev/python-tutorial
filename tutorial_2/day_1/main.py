from datetime import datetime
from json import load
from tkinter import (
    Canvas,
    Frame,
    Label,
    PhotoImage,
    Scrollbar,
    Tk,
)

from requests import get

root = Tk()
root.title("Weather app: Day 1")
root.geometry("300x300")
root.resizable(False, False)

frame = Frame(root)
frame.pack()

response = get("https://ipinfo.io/loc")
if response.status_code != 200:
    print("Failed to get location")
    exit(1)
lat, lon = response.text.split(",")

today = datetime.now()

# response = get(
#     "https://api.openweathermap.org/data/3.0/onecall",
#     params={
#         'lat': round(float(lat), 2),
#         'lon': round(float(lon), 2),
#         # 'date': today.strftime("%Y-%m-%d"),
#         'exclude': "current,minutely,daily,alerts",
#         'units': "metric",
#         'appid': "e54abbee525c90e62c1587e6d90a6407"
#     }
# )
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

# with open("response.json", "w") as f:
#     f.write(response.text)

with open("response.json", "r") as f:
    data = load(f)

my_location_label = Label(frame, text="MY LOCATION", font=("Helvetica", 16, "bold"), anchor="n", pady=10)
my_location_label.pack()

location_label = Label(frame, text=data['timezone'], font=("Helvetica", 16), anchor="n")
location_label.pack()

# scrollbar = Scrollbar(frame)
# scrollbar.pack(side="top", fill="x")

canvas = Canvas(frame)
canvas.pack()

for weather in data['hourly']:
    dt = datetime.fromtimestamp(weather['dt'])
    if dt.day == today.day and dt.month == today.month and dt.year == today.year:
        image = PhotoImage(data=get(f"https://openweathermap.org/img/wn/{weather['weather'][0]['icon']}.png").content)
        canvas.create_image(0, 0, image=image, anchor="nw")
        canvas.create_text(50, 0, text=datetime.fromtimestamp(weather['dt']).strftime("%H:%M"))
        canvas.create_text(50, 20, text=f"Temp: {weather['temp']}°C")

root.mainloop()
