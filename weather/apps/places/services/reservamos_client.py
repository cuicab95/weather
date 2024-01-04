import requests
from unidecode import unidecode
from .open_weather_client import OpenWeatherClient


class ReservamosClient:

    def __init__(self):
        self.__url_client = "https://search.reservamos.mx/api/v2"

    def get_places(self, search):
        headers = {}
        search = unidecode(search)
        params = f"?q={search}"
        url = f"{self.__url_client}/places{params}"
        response = requests.get(url=url, headers=headers)
        data = response.json()
        return self.filter_data_by_result_type(data, search)

    @classmethod
    def filter_data_by_result_type(cls, data, search):
        data = filter(lambda d: d['result_type'] == "city" and d['country'] == "México" and search in d['city_slug'], data)
        return cls.get_lat_and_long(list(data))

    @classmethod
    def get_lat_and_long(cls, data):
        result = []
        for item in data:
            weather_data = OpenWeatherClient().get_weather_by_lat_and_long(
                item['lat'],
                item['long']
            )
            result.append({
                'city_name': item.get("display", ""),
                'state': item.get("state", ""),
                'country': item.get("country", ""),
                'lat': item.get("lat", ""),
                'long': item.get("long", ""),
                **weather_data
            })
        return result

