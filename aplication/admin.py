from django.contrib import admin

from  aplication.models import Forums, News, Publisher

# Register your models here.
admin.site.register(Forums)
admin.site.register(News)
admin.site.register(Publisher)