# Generated by Django 4.2.5 on 2024-09-12 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=30)),
                ('Professor', models.CharField(max_length=30)),
                ('Day', models.CharField(max_length=15)),
                ('Time', models.CharField(max_length=15)),
            ],
        ),
    ]
