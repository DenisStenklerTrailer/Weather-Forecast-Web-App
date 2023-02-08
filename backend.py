import requests

API_key = "141710af2113bab9f55ef73e1bcd33d5"

def get_data(place, days, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    content = response.json()
    filtered_content = content['list']
    filtered_content = filtered_content[:8 * days]

    return filtered_content

if __name__ == "__main__":
    print(get_data(place="Koritnica", days=2))
