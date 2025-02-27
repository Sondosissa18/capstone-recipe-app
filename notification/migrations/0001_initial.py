# Generated by Django 3.1.5 on 2021-01-19 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipe_user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('viewed', models.BooleanField(default=False)),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_user.message')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
