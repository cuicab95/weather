from django.test import TestCase

# Create your tests here.


class WeatherTestCase(TestCase):
    def setUp(self):
        self.__url_api = "http://localhost:8000/weather/get-weather-by-place/"

    def test_get_temp_of_merida(self):
        params = "?q=merida"
        result = self.client.get(f"{self.__url_api}{params}")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data[0]["city_name"], "Mérida")
        self.assertEqual(result.data[0]["country"], "México")
        self.assertEqual(len(result.data[0]["daily"]), 8)

    def test_params_is_required(self):
        params = ""
        result = self.client.get(f"{self.__url_api}{params}")
        self.assertEqual(result.status_code, 400)
        self.assertEqual(len(result.data["q"]), 1)
