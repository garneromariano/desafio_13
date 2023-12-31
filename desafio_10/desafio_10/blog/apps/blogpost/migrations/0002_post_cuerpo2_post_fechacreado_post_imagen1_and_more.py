# Generated by Django 4.2.1 on 2023-07-23 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cuerpo2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='fechaCreado',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='imagen1',
            field=models.ImageField(null=True, upload_to='blogpost/'),
        ),
        migrations.AddField(
            model_name='post',
            name='imagen2',
            field=models.ImageField(null=True, upload_to='blogpost/'),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='titulo2',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
