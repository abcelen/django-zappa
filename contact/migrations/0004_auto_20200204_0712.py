# Generated by Django 2.2.9 on 2020-02-04 07:12

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('contact', '0003_auto_20200204_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='head_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='summary',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
