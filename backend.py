import requests

API_key = "141710af2113bab9f55ef73e1bcd33d5"

def get_data(place, days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    content = response.json()
    return content

if __name__ == "__main__":
    print(get_data(place="Koritnica"))