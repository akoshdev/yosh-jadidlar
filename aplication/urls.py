from django.urls import path
from aplication.views import GenericView, AboutView, forums, forum_detail, news_detail, ScientificView
app_name = 'aplication'


urlpatterns = [
    path('', forums, name='home'),
    path('generic/', GenericView.as_view(), name='generic'),
    path('about/', AboutView.as_view(), name='about'),
    path('ilmiy-jurnal/', ScientificView.as_view(), name='ilmiy'),
    path('forum/<int:id>/', forum_detail, name='forum-detail'),
    path('new/<int:id>/', news_detail, name='new-detail'),
]