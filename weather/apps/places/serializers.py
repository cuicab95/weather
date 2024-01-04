from rest_framework import serializers


class WeatherSearchSerializer(serializers.Serializer):
    q = serializers.CharField()
