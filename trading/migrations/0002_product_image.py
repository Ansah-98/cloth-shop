# Generated by Django 4.0.2 on 2022-06-19 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='cart.png', upload_to=''),
        ),
    ]