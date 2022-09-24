import requests
from requests import get
import sys

def main():
    menu()

#menu choice for user. Choice A for getting Public IP, choice B for getting IP LOC info, choice Q is exit.
def menu():
    choice = input("""
    A: Get your Public IP
    B: Get IP Location Information
    Q: Exit

    Please enter your choice: """)

    if choice == "A" or choice =="a":
        get_public_ip()
    elif choice == "B" or choice =="b":
        get_ip_location()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()

#code for getting the public ip of the user.
def get_public_ip():
    ip = get('https://api.ipify.org').text
    print('Your public IP address is: {}'.format(ip))

#code for getting the location information of the ip address that the user inputs.
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
    return print(ip_location_data) 

main()
