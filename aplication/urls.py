from django.urls import path
from aplication.views import GenericView, AboutView, forums, forum_detail, news_detail, public, public_detail, \
    nashriyot, nashriyot_haqida, nashriyot_faoliyati, nashriyot_afzalliklari

app_name = 'aplication'

urlpatterns = [
    path('', forums, name='home'),
    path('generic/', GenericView.as_view(), name='generic'),
    path('haqida/', AboutView.as_view(), name='about'),
    path('nashriyot/', nashriyot, name='nashriyot'),
    path('ilmiy-jurnal/', public, name='public'),
    path('index.php.ilmiy-jurnal/<int:id>/', public_detail, name='public-detail'),
    path('forum/<int:id>/', forum_detail, name='forum-detail'),
    path('new/<int:id>/', news_detail, name='new-detail'),
    path('nashriyot-haqida/', nashriyot_haqida, name='nashriyot-haqida'),
    path('nashriyot-faoliyati/', nashriyot_faoliyati, name='nashriyot-faoliyati'),
    path('nashriyot-afzalliklari/', nashriyot_afzalliklari, name='nashriyot-afzalliklari'),
]
