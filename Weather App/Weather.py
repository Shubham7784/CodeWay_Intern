import requests as rs
import xml.etree.ElementTree as xp
from tkinter import *
from tkinter import ttk

def main():

    location = input("Enter you city name or city ZIP code : ")
    api_key = "5b2174165cf64cf598e95646240402"
    try:
        data = rs.get(f"http://api.weatherapi.com/v1/current.xml?key={api_key}&q={location}").content
        with open(r'CodeWay_Intern\Weather App\weather.xml','wb') as f:
            f.write(data)
            f.close()
    except Exception as e:
        print(e)
    
    try:
        data = xp.parse(r"CodeWay_Intern\Weather App\weather.xml")
        data = data.getroot()
        if(data.tag == "error"):
            message = data.findall("*")
            code = message[0].text
            message = message[1].text
            print(f"Error Code : {code}\nMessage : {message}")
            return
        data = data.findall("*")
        l = data[0]
        c_name = l.find("name").text
        reg = l.find("region").text
        cont = l.find("country").text
        time = l.find("localtime").text
        curr = data[1]
        temp_c = curr.find("temp_c").text
        temp_c+= chr(176)+"C"
        temp_f = curr.find("temp_f").text
        temp_f+= chr(176)+"F"
        humid = curr.find("humidity").text
        cond = curr.find("condition")
        cond = cond.find("text").text
        wind_s = curr.find("wind_kph").text
        wind_s+= "kph"
        window = Tk()
        window.title("Weather Update")
        window.minsize(500,300)
        window.maxsize(500,300)
        city_label = Label(window,text=f"City: {c_name}",font=("calibri",20))
        city_label.pack()
        region_label = Label(window,text=f"State : {reg} | Country : {cont}",font=("calibri",15))
        region_label.pack()
        sep = ttk.Separator(window,orient="horizontal")
        sep.pack(fill="x")
        main_label = Label(window,text="Weather Report",font=("algerian",20))
        main_label.pack()
        cond_label = Label(window,text=cond,font=("calibri",15))
        cond_label.pack()
        temp_label = Label(window,text=f"Tempratue : {temp_c} OR {temp_f}",font=("calibri",15))
        temp_label.pack()
        humid_label = Label(window,text=f"Humidity : {humid}",font=("calibri",15))
        humid_label.pack()
        wind_label = Label(window,text=f"Wind Speed : {wind_s}",font=("calibri",15))
        wind_label.pack()
        window.mainloop()
    except Exception as e:
        print(e)
    


if __name__ == "__main__":
    main()