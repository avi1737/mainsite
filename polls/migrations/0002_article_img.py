# Generated by Django 2.2.4 on 2019-12-08 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ImageField(default='', upload_to='polls/images/'),
        ),
    ]