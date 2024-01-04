from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .services.reservamos_client import ReservamosClient


class GetWeatherByPlaceAPIView(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        search = request.GET.get('q', "")
        client = ReservamosClient()
        data = client.get_places(search)
        return Response(data)
