from rest_framework import serializers


class CountrySerializer(serializers.Serializer):
    name = serializers.CharField()
    capital = serializers.CharField()
    flag_url = serializers.CharField(source='flags')
