# Generated by Django 4.2.4 on 2023-09-05 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miLibreria', '0006_remove_libro_id_alter_libro_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='numeroCli',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]