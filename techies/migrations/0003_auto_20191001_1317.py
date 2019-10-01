# Generated by Django 2.1.11 on 2019-10-01 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techies', '0002_coguser'),
    ]

    operations = [
        migrations.AddField(
            model_name='coguser',
            name='email',
            field=models.CharField(default='x', max_length=150, unique=True),
        ),
        migrations.AddField(
            model_name='coguser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]