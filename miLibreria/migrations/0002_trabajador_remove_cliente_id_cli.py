# Generated by Django 4.2.4 on 2023-08-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miLibreria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_trabj', models.CharField(max_length=200)),
                ('nombreTrabj', models.CharField(max_length=200)),
                ('telefonoTraj', models.CharField(max_length=10)),
                ('corrreoTrabj', models.EmailField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='id_Cli',
        ),
    ]
