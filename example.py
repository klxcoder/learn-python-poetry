import requests

def get_ip_info():
    response = requests.get("https://api.ipify.org?format=json")
    if response.status_code == 200:
        data = response.json()
        print(f"Your IP address is: {data['ip']}")
    else:
        print("Failed to retrieve IP address.")

if __name__ == "__main__":
    get_ip_info()
