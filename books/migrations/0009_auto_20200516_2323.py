# Generated by Django 2.2.4 on 2020-05-16 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20200516_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_image',
            new_name='book_img',
        ),
    ]
