# Generated by Django 2.1.5 on 2021-11-26 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_herb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AddField(
            model_name='post',
            name='PostId',
            field=models.AutoField(null=True, serialize=False),
            preserve_default=False,
        ),
    ]