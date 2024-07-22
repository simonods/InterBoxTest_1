import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CountrySerializer
from tabulate import tabulate
from django.shortcuts import render


class CountryListView(APIView):
    def get(self, request):
        api_url = 'https://restcountries.com/v3.1/all'
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()

            countries = [
                {
                    'name': country.get('name', {}).get('common', 'N/A'),
                    'capital': country.get('capital', ['N/A'])[0],
                    'flags': country.get('flags', {}).get('png', 'N/A')
                }
                for country in data
            ]

            table = tabulate(countries, headers='keys', tablefmt='pretty')
            print(table)

            serializer = CountrySerializer(countries, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except requests.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
