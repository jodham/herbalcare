# Generated by Django 2.1.5 on 2021-11-25 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20211124_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Herb',
            fields=[
                ('HerbId', models.AutoField(primary_key=True, serialize=False)),
                ('HerbName', models.CharField(max_length=40)),
                ('diseaseName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Disease')),
            ],
        ),
    ]
