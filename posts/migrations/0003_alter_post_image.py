# Generated by Django 3.2.14 on 2022-08-03 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_rgq6aq', upload_to='images/'),
        ),
    ]
