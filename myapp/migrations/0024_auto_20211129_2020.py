# Generated by Django 2.1.5 on 2021-11-29 20:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_auto_20211129_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disease',
            name='doc',
        ),
        migrations.AddField(
            model_name='herb',
            name='HerbPhoto',
            field=models.ImageField(default='default.jpeg', upload_to='HerbPhotos'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
