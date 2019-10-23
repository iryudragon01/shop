# Generated by Django 2.2.6 on 2019-10-23 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.PositiveIntegerField()),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'ticket'), (2, 'Air Pay'), (3, 'food')])),
            ],
        ),
        migrations.CreateModel(
            name='Top_up',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.PositiveIntegerField()),
                ('worker', models.CharField(max_length=200)),
                ('date_fillup', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Last_update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.PositiveIntegerField()),
                ('Last_stock', models.PositiveIntegerField()),
                ('date_log', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Display_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.PositiveIntegerField()),
                ('latest', models.PositiveIntegerField()),
                ('price_tag', models.PositiveIntegerField()),
                ('price_volume', models.PositiveIntegerField()),
                ('sum_volume', models.PositiveIntegerField()),
                ('version', models.PositiveIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Item')),
            ],
        ),
    ]
