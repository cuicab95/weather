# weather
Challenge Python Software Engineer | Reservamos

Dependencias:
- Python 3.11.2
- Docker
- Django 5.0.1


Para configurar el proyecto de manera local:
- git clone https://github.com/cuicab95/weather.git
- docker-compose up --build --> Compilar/configurar el proyecto

La api es:
- http://localhost:8000/weather/get-weather-by-place/?q=merida
- Es tipo GET
- Es una api pública (no es necesario login)


Para correr los tests:
- docker-compose run web python manage.py test
