import requests

API_key = "141710af2113bab9f55ef73e1bcd33d5"

def get_data(place, days, kind):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    content = response.json()
    filtered_content = content['list']
    filtered_content = filtered_content[:8 * days]

    if kind == "Temperature":
        filtered_content = [temp['main']['temp'] for temp in filtered_content]
    elif kind == "Sky":
        filtered_content = [sky['weather'][0]['main'] for sky in filtered_content]

    return filtered_content

if __name__ == "__main__":
    print(get_data(place="Koritnica", days=2, kind="Sky"))
