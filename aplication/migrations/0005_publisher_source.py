# Generated by Django 5.2 on 2025-04-19 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0004_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='source',
            field=models.TextField(blank=True, null=True, verbose_name='Foydalanilgan adabiyotlar'),
        ),
    ]
