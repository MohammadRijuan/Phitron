# Generated by Django 5.1 on 2024-09-02 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(max_length=200)),
                ('Skills', models.CharField(choices=[('teamwork', 'teamwork'), ('leader', 'leader'), ('management', 'management')], max_length=50)),
            ],
        ),
    ]
