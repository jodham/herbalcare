# Generated by Django 2.1.5 on 2021-11-29 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_auto_20211129_1926'),
    ]

    operations = [
        migrations.DeleteModel(
            name='status',
        ),
        migrations.AlterField(
            model_name='diseasestatus',
            name='statusDescription',
            field=models.CharField(max_length=100),
        ),
    ]
