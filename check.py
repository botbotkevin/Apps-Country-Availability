import sys
import json
import requests

country_codes_url = "https://raw.githubusercontent.com/jcoester/iTunes-country-codes/main/itunes_country_codes.json"
country_response = requests.get(country_codes_url)

if country_response.status_code == 200:
    country_dict = country_response.json()
else:
    print("Failed to retrieve data:", country_response.status_code)

def check_available_countries(app_id):
    available_countries = []
    for key in country_dict.keys():
        url = "https://apps.apple.com/{0}/app/id{1}".format(key.lower(), app_id)
        app_response = requests.get(url)
        app_content = app_response.content.decode('utf-8')
        if app_id in app_content:
            available_countries.append(country_dict[key])
    if len(available_countries) >= 1:
        print('\n'.join(available_countries))
    else:
        print("No available countries!")

if len(sys.argv) == 1:
    print("Please enter an app id!")
else:
    check_available_countries(sys.argv[1])
