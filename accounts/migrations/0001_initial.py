# Generated by Django 3.0.5 on 2022-01-08 03:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biography', models.TextField()),
                ('location', models.CharField(max_length=150)),
                ('website', models.URLField()),
                ('date_birth', models.DateTimeField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('background_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
