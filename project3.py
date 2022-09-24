import requests
from requests import get

def get_public_ip():
    ip = get('https://api.ipify.org').text
    print('My public IP address is: {}'.format(ip))

def get_ip_location():
    ip_address = input("input your IP Address: ")
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    ip_location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "country code": response.get("country_code"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude"),
        "asn": response.get("asn"),
        "isp":response.get("isp")
    }
    return ip_location_data

get_public_ip()

print(get_ip_location())

