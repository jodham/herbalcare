# Generated by Django 2.1.5 on 2021-11-19 08:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='herbalist',
            name='HerbalistContact',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='post',
            name='HerbalistID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Herbalist'),
        ),
    ]
