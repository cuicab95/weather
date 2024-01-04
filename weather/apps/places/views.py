from rest_framework.views import APIView
from rest_framework.response import Response
from .services.reservamos_client import ReservamosClient
from .serializers import WeatherSearchSerializer


class GetWeatherByPlaceAPIView(APIView):
    permission_classes = []
    serializer_class = WeatherSearchSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.GET)
        serializer.is_valid(raise_exception=True)
        search = serializer.validated_data["q"]
        client = ReservamosClient()
        data = client.get_places(search)
        return Response(data)
