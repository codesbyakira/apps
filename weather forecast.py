#import modules required
from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox
api_key='f3b21dca640461a3d3a66facbd561415'
url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
#function to get weather details

def getweather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin-273.15
        weather1 = json['weather'][0]['main']
        final = [city, country, temp_kelvin, temp_celsius, weather1]
        return final
    else:
        print("No Content Found")

#function to search city
def search():
    city = city_text.get()
    weather = getweather(city)
    if weather:
        location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
        temp_lbl['text'] = str(weather[3])+"  Degree Celsius"        
        weather_lbl['text'] = weather[4]
    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))


tk=Tk()
tk.title("Weather Forecast")
tk.geometry("500x300")
tk.configure(bg="#87CEEB")
my_image=PhotoImage(file='C:/Users/user/Desktop/WOW.png')
lbl=Label(image=my_image).pack()
frame=Frame(tk,width=350,height=350,bg="#87CEEB")
frame.place(x=480,y=70)
city_text=StringVar()
city_entry=Entry(tk, textvariable=city_text)
city_entry.pack()
Search_btn=Button(tk, text="search weather", width=12, command=search)
Search_btn.pack()
location_lbl=Label(tk, text="location",font={"bold,20"})
location_lbl.pack()
temp_lbl=Label(tk, text="")
temp_lbl.pack()
weather_lbl=Label(tk, text="")
weather_lbl.pack()

tk.mainloop()
