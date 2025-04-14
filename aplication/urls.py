from django.urls import path
from aplication.views import IndexView
app_name = 'aplication'


urlpatterns = [
    path('', IndexView.as_view(), name='home'),

    ]