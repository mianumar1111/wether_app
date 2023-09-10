import tkinter as tk
from tkinter import Tk
from tkinter import ttk
import requests
import json


win = tk.Tk()
win.title('Whether App')

label1 = tk.Label(win,text='Please enter the Location: ',borderwidth=1,relief='solid',background='white')
label1.grid(row=1,column=1,sticky='w',padx=3,pady=3)

Temp_Label = tk.Label(win,text=f'Location Details : ',borderwidth=1,relief='solid',background='white')
Temp_Label.grid(row=2,column=1,sticky='w',padx=3,pady=3)

Temp_Label = tk.Label(win,text=f'The Temp at location : ',borderwidth=1,relief='solid',background='white')
Temp_Label.grid(row=3,column=1,sticky='w',padx=3,pady=3)

humidity_Label = tk.Label(win,text='The Humidity of location is : ',borderwidth=1,relief='solid',background='white')
humidity_Label.grid(row=4,column=1,sticky='w',padx=3,pady=3)

wind_kph_Label = tk.Label(win,text='The speed of Wind in KPH is : ',borderwidth=1,relief='solid',background='white')
wind_kph_Label.grid(row=5,column=1,sticky='w',padx=3,pady=3)

Cloud_Label = tk.Label(win,text='Couds the location are: ',borderwidth=1,relief='solid',background='white')
Cloud_Label.grid(row=6,column=1,sticky='w',padx=3,pady=3)

location = tk.StringVar()
entery_Box1 = tk.Entry(win,width=13,textvariable=location)
entery_Box1.grid(row=1,column=2)

temp_type_label = tk.Label(win,text='Select Temp unit: ',borderwidth=1,relief='solid',background='white')
temp_type_label.grid(row=7,column=1,sticky='w',padx=3,pady=3)

temp_type_menu =tk.StringVar()
temp_type_menu = ttk.Combobox(win,width=13,values=['F','C'])
temp_type_menu.grid(row=7,column=2)


def action():
    try:
        
        url = f'https://api.weatherapi.com/v1/current.json?key=63166dbdee5d4c4cad4212358231009&q={location.get()}'

        r = requests.get(url)
        load_data = json.loads(r.text)
        if temp_type_menu.get() == 'F':
            Temp = load_data['current']['temp_f']
            Temp_Label = tk.Label(win,text=f'{Temp} F',borderwidth=1,relief='solid',font='bold',background='white')
            Temp_Label.grid(row=3,column=2,sticky='w',padx=3,pady=3)
        
        else:
            Temp = load_data['current']['temp_c']
            Temp_Label = tk.Label(win,text=f'{Temp} C',borderwidth=1,relief='solid',font='bold',background='white')
            Temp_Label.grid(row=3,column=2,sticky='w',padx=3,pady=3)
            
        humidity = load_data['current']['humidity']
        wind_kph = load_data['current']['wind_kph']
        cloud = load_data['current']['cloud']
        location_name = load_data['location']['name']
        region = load_data['location']['region']
        country = load_data['location']['country']
        date_time = load_data['location']['localtime']
        full_Location = f'{location_name}, {region}, {country}. Time is: {date_time}'
        
        full_Location_label = tk.Label(win,text=full_Location,borderwidth=1,relief='solid',font='bold',background='white')
        full_Location_label.grid(row=2,column=2,sticky='w',padx=3,pady=3)

        humidity_Label = tk.Label(win,text=f'{humidity}%',borderwidth=1,relief='solid',font='bold',background='white')
        humidity_Label.grid(row=4,column=2,sticky='w',padx=3,pady=3)

        wind_kph_Label = tk.Label(win,text=wind_kph,borderwidth=1,relief='solid',font='bold',background='white')
        wind_kph_Label.grid(row=5,column=2,sticky='w',padx=3,pady=3)

        Cloud_Label = tk.Label(win,text=cloud,borderwidth=1,relief='solid',font='bold',background='white')
        Cloud_Label.grid(row=6,column=2,sticky='w',padx=3,pady=3)
    except:
        error_lbl = tk.Label(win,text='Sorry!, location not fount',borderwidth=1,relief='solid',font='bold',background='white')
        error_lbl.grid(row=2,column=2,padx=3,pady=3)
        
        
btn = tk.Button(win,text='Search',command=action,width=14,foreground='Black',background='white')
btn.grid(columnspan=2)



win.mainloop()