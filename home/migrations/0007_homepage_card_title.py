# Generated by Django 2.2.9 on 2020-02-02 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homepage_slides'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='card_title',
            field=models.CharField(default='Title', max_length=100, null=True),
        ),
    ]
