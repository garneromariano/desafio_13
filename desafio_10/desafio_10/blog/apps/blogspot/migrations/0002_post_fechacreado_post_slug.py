# Generated by Django 4.2.1 on 2023-07-23 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogspot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fechaCreado',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
