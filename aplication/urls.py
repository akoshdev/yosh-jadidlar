from django.urls import path
from aplication.views import IndexView, GenericView
app_name = 'aplication'


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('generic/', GenericView.as_view(), name='generic'),

    ]