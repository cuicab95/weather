import requests


class OpenWeatherClient:

    def __init__(self):
        self.__url_client = "https://api.openweathermap.org/data/2.5"
        self.__api_key = "a5a47c18197737e8eeca634cd6acb581"

    def get_weather_by_lat_and_long(self, lat, long):
        headers = {}
        params = f"?lat={lat}&lon={long}&exclude=minutely,hourly&appid={self.__api_key}&lang=es&units=metric"
        url = f"{self.__url_client}/onecall{params}"
        response = requests.get(url=url, headers=headers)
        data = response.json()
        return self.clear_data(data)

    @classmethod
    def clear_data(cls, data):
        temp_data = cls.get_min_and_max_temp(data)
        return {'daily': temp_data}

    @classmethod
    def get_min_and_max_temp(cls, data):
        result = []
        for temp in data.get("daily", []):
            result.append({
                'temp_min': temp['temp']['min'],
                'temp_max': temp['temp']['max'],
                'weather': temp['weather'][0]['description'],
            })
        return result

