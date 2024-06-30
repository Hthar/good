import requests


weather_warnings_alert = {
    "wind": "It is windy. Avoid areas with power lines as they may be dangerous.\n",
    "rain": "It is raining. Carry an umbrella and be careful of slippery roads. If possible, don't go outside.\n",
    "drizzle": "It is drizzling. Carry an umbrella and be cautious of slippery roads.\n",
    "clear": "The weather is good. Have a great day!\n",
    "clouds": "It is probably raining. It is nice living in a cloudy area.\n",
    "humidity": "High humidity can make you feel uncomfortable, so try to be active if you are feeling dull.\n",
    "normal": "The temperature is normal. Enjoy your day!\n",
    "snow": "It is too cold to go outside. If possible, stay at home warmly.\n",
    "sun": "It can be hot. If it is too hot, you can get heatstroke, so be careful and stay safe.\n"
}

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    api_key ="50dc0a5390b7b6728f51dbe56d7a2465"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    print(response)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        condition = data["weather"][0]["main"].lower()
        return temp, condition
    

def weather_temp_alert(temp):
    if temp > 39:
        print("Attention! Temperature is above 39 degrees Celsius. Extreme heat poses health risks including\n" 
              "dehydration and heatstroke.Stay hydrated, seek shade or air-conditioned spaces, and avoid strenuous activities\n"
               "outdoors during peak hours to ensure your well-being.\n")
    elif 30 < temp <= 39:
        print("Attention: The temperature is above 30 degrees Celsius and is hotter than normal. If you are going outside, \n"
              "wear a hat and use sunscreen on your face. Don't forget to drink water as much as possible!\n")
    elif 20 <= temp <= 30:
        print("Normal: The temperature is normal being between 20 degree celcius and 30  degree celcius .\n"
              "Enjoy your day. It is a little hot, please drink water as much as possible,\n "
              "with a suggestion to drink 8 bottles per day. And if you are going outside, don't forget to take an umbrella.\n")
    elif temp < 20:
        print("Cold: The temperature is below 20 degrees Celsius. It's cool, so dress warmly.\n"
              "If possible, try to drink water as much as possible.\n")
    else:
        print("No data\n")

try:
    city = input("Enter the city (Yangon, Mandalay, Naypyidaw, Sagaing, Magway, London, Osaka, Yakutsk, Oymyakon): ").title()

    if city not in ["Yangon", "Mandalay", "Naypyidaw", "Sagaing", "Magway", "London", "Osaka", "Yakutsk", "Oymyakon"]:
        print("City not found. Please enter a valid city.")
    else:
        temp, condition = get_weather(city)
        
        if temp is not None and condition is not None:
            print(f"\nThe current temperature in {city} is {temp} degrees Celsius.\n")
            try:
                warning_msg = weather_warnings_alert[condition]
            except KeyError:
                warning_msg = "No Data \n"
            print(f"In {city}...\n{warning_msg}")
            weather_temp_alert(temp)
        else:
            print("Could not upload the weather data. Please try again later.")



    power_outage = input("\nIs there a power outage? (yes/no): ").lower() == 'yes'
    if power_outage:
        print("\nThis is not good news. Calm down a bit! If you want to express your frustration at the EPC,\n "
              "say 'FUck EPC!!!' in order to reduce your anger and stress.\n")
    else:
        print("There is good news. I hope you will pass through your day happily without difficulties and\n" 
              "stress caused by the EPC.")

except ValueError:
    print("Invalid input.")
