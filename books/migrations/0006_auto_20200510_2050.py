# Generated by Django 2.2.4 on 2020-05-10 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20200510_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_img',
            field=models.ImageField(default=True, upload_to='images'),
        ),
    ]