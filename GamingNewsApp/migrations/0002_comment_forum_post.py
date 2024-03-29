# Generated by Django 2.2 on 2021-06-07 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GamingNewsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=1000)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_messages', to='GamingNewsApp.User')),
                ('user_likes', models.ManyToManyField(related_name='liked_posts', to='GamingNewsApp.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('forum_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='GamingNewsApp.Forum_Post')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to='GamingNewsApp.User')),
            ],
        ),
    ]
