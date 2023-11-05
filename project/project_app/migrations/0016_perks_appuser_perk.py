# Generated by Django 4.2.7 on 2023-11-04 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0015_alter_killer_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='media/perks/')),
            ],
        ),
        migrations.AddField(
            model_name='appuser',
            name='perk',
            field=models.ManyToManyField(related_name='users', to='project_app.perks'),
        ),
    ]
