# Generated by Django 3.0.4 on 2020-11-16 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Segment', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('Product', models.CharField(max_length=100)),
                ('Units', models.CharField(max_length=100)),
                ('Sales', models.CharField(max_length=100)),
                ('Datesold', models.CharField(max_length=100)),
            ],
        ),
    ]
