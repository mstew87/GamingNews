# Generated by Django 2.2 on 2021-06-10 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamingNewsApp', '0008_auto_20210609_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='../Full-Stack-Django-Project/images/default.jpg', null=True, upload_to='../Full-Stack-Django_project/images'),
        ),
    ]
