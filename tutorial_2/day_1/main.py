from datetime import datetime
from io import BytesIO
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
root.geometry("440x440")
# root.resizable(False, False)

frame = Frame(root)
frame.pack()

response = get("https://ipinfo.io/loc")
if response.status_code != 200:
    print("Failed to get location")
    exit(1)
lat, lon = response.text.split(",")

today = datetime.now()

response = get(
    "https://api.openweathermap.org/data/3.0/onecall",
    params={
        'lat': round(float(lat), 2),
        'lon': round(float(lon), 2),
        'exclude': "current,minutely,daily,alerts",
        'units': "metric",
        'appid': "e54abbee525c90e62c1587e6d90a6407"
    }
)
data = response.json()

my_location_label = Label(frame, text="MY LOCATION", font=("Helvetica", 16, "bold"), anchor="n", pady=10)
my_location_label.pack()

location_label = Label(frame, text=data['timezone'], font=("Helvetica", 16), anchor="n")
location_label.pack()

weather_hourly_canvas = Canvas(frame, height=110)
weather_hourly_canvas.pack()

scrollbar = Scrollbar(frame, orient="horizontal", command=weather_hourly_canvas.xview)
scrollbar.pack(fill="x")

weather_hourly_canvas.configure(xscrollcommand=scrollbar.set)
weather_hourly_canvas.bind(
    "<Configure>",
    lambda e: weather_hourly_canvas.configure(scrollregion=weather_hourly_canvas.bbox("all"))
)

weather_hourly_frame = Frame(weather_hourly_canvas)
weather_hourly_canvas.create_window((0, 0), window=weather_hourly_frame)

column = 0
cards = {}
for weather in data['hourly']:
    dt = datetime.fromtimestamp(weather['dt'])
    if dt.day == today.day and dt.month == today.month and dt.year == today.year:
        with open(f"icons/{weather['weather'][0]['icon']}.png", "wb") as f:
            f.write(get(f"https://openweathermap.org/img/wn/{weather['weather'][0]['icon']}.png").content)
        cards[dt.strftime("%H:%M")] = {}
        cards[dt.strftime("%H:%M")]['frame'] = Frame(weather_hourly_frame, padx=10, pady=10)
        cards[dt.strftime("%H:%M")]['frame'].grid(row=0, column=column)
        cards[dt.strftime("%H:%M")]['image_frame'] = Frame(cards[dt.strftime("%H:%M")]['frame'])
        cards[dt.strftime("%H:%M")]['image_frame'].pack()
        cards[dt.strftime("%H:%M")]['image'] = PhotoImage(file=f"icons/{weather['weather'][0]['icon']}.png")
        image_label = Label(
            cards[dt.strftime("%H:%M")]['image_frame'],
            bg="#6bc6fa",
            image=cards[dt.strftime("%H:%M")]['image'],
        )
        image_label.pack()
        time_label = Label(cards[dt.strftime("%H:%M")]['frame'], text=dt.strftime("%H:%M"))
        time_label.pack()
        temp_label = Label(cards[dt.strftime("%H:%M")]['frame'], text=f"{round(weather['temp'])}°C")
        temp_label.pack()
        column += 1

root.mainloop()
