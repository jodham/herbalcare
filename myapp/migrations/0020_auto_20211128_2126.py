# Generated by Django 2.1.5 on 2021-11-28 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20211126_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disease',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='title',
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(null=True),
        ),
    ]