# Generated by Django 3.2.6 on 2021-08-24 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='Image/None/noimg.jpg', upload_to='Image/'),
        ),
    ]
