# Generated by Django 3.0.5 on 2022-01-11 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twit', '0003_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
