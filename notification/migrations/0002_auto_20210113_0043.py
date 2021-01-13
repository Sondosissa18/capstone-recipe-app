# Generated by Django 3.1.5 on 2021-01-13 00:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notification', '0001_initial'),
        ('recipe_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_user.message'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
