# Generated by Django 2.2.6 on 2019-10-26 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=120)),
                ('username', models.CharField(max_length=200)),
                ('password1', models.CharField(max_length=200)),
                ('password2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User_Start_Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('date_log', models.DateTimeField()),
            ],
        ),
    ]
