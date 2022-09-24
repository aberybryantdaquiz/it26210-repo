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
    ip = get('https://api.ipify.org').text #used the api of ipify in order to get the public ip address of the user
    print('\nYour public IP address is: {}'.format(ip)) #prints the public ip address

#code for getting the location information of the ip address that the user inputs.
def get_ip_location():
    ip_address = input("\ninput your IP Address: ") #user input for getting ip address
    #used the api of ipapi in order to get the different data for the ip address that the user inputted.
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json() 
    #ip_location_data houses all the data that came from the ipapi api then prints so that the user can see.
    ip_location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "country code": response.get("country_code"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude"),
        "asn": response.get("asn"),
        "isp": response.get("isp")
    }
    return print(ip_location_data)

main()
