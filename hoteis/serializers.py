from rest_framework import serializers
from hoteis.models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Hotel
