# Generated by Django 4.1.3 on 2022-11-11 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=256)),
                ('senha', models.CharField(max_length=256)),
                ('data_nascimento', models.DateField()),
            ],
        ),
    ]
