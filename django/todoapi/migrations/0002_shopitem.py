# Generated by Django 2.1.4 on 2020-10-18 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=255)),
                ('town', models.CharField(max_length=50)),
                ('zipCode', models.CharField(max_length=5)),
            ],
        ),
    ]