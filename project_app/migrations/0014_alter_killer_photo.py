# Generated by Django 4.2.7 on 2023-11-04 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0013_killer_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='killer',
            name='photo',
            field=models.ImageField(upload_to='killers'),
        ),
    ]
