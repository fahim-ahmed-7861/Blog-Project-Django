# Generated by Django 3.2 on 2021-04-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(default=1, upload_to='blog_images', verbose_name='Image'),
            preserve_default=False,
        ),
    ]
