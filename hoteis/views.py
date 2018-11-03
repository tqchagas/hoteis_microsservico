from hoteis.models import Hotel
from hoteis.serializers import HotelSerializer
from rest_framework import generics


class HotelCriarListar(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelDetalheApagar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
