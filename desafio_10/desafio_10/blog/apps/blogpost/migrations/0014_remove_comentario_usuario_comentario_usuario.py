# Generated by Django 4.2.1 on 2023-07-27 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogpost', '0013_comentario_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='usuario',
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
