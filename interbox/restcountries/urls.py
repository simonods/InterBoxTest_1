from django.urls import path
from .views import *

urlpatterns = [
    path('countries/', CountryListView.as_view(), name='country_list'),
]
