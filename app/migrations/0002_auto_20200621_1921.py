# Generated by Django 2.2.13 on 2020-06-22 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fechanacimiento',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='grado',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=1),
        ),
    ]
