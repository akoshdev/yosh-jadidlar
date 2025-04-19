from django.db import models

# Create your models here.

class Forums(models.Model):
    image = models.ImageField(upload_to='main_images', verbose_name='Rasm tanlang')
    title = models.CharField(max_length=255, verbose_name='Nomini kiriting')
    min_desc = models.CharField(max_length=255, verbose_name="Qisqacha ma'zmuni")
    description = models.TextField(verbose_name="To'liq ma'zmunini kiriting")
    tg_username = models.CharField(max_length=255, null=True, blank=True, verbose_name="Bog'lanish uchun telegram username")

    class Meta:
        verbose_name = 'Tadbir'
        verbose_name_plural = 'Tadbirlar'

    def __str__(self):
        return self.title

class News(models.Model):
    image = models.ImageField(upload_to='main_images', verbose_name='Rasm tanlang')
    title = models.CharField(max_length=255, verbose_name='Nomini kiriting')
    min_desc = models.CharField(max_length=255, verbose_name="Qisqacha ma'zmuni")
    description = models.TextField(verbose_name="To'liq ma'zmunini kiriting")
    tg_username = models.CharField(max_length=255, null=True, blank=True,
                                   verbose_name="Bog'lanish uchun telegram username")

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'

    def __str__(self):
        return self.title

class Publisher(models.Model):
    image = models.ImageField(upload_to='main_images', verbose_name='Rasm tanlang', blank=True)
    title = models.CharField(max_length=255, verbose_name='Nomini kiriting')
    annotatsiya = models.TextField(verbose_name="Annotatsiya")
    keywords = models.TextField(verbose_name="Kalit so'zlar")
    abstract = models.TextField(verbose_name="Abstarct")
    keywords2 = models.TextField(verbose_name="Keywords")
    description = models.TextField(verbose_name="To'liq ma'zmunini kiriting")
    source = models.TextField(verbose_name="Foydalanilgan adabiyotlar", blank=True, null=True)

    class Meta:
        verbose_name = 'Nashriyot'
        verbose_name_plural = 'Nashriyotlar'

    def __str__(self):
        return self.title