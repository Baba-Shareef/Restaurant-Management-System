# Generated by Django 4.2.5 on 2023-09-27 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_veglunch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vegdinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.CharField(max_length=20)),
                ('Price', models.IntegerField()),
            ],
        ),
    ]
