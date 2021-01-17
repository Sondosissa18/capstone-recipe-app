# Generated by Django 3.1.5 on 2021-01-17 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('items', models.TextField(default='ingredients', max_length=140)),
                ('timerequired', models.CharField(max_length=100)),
                ('instructions', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('category', models.CharField(choices=[('BREAKFAST', 'Breakfast'), ('LUNCH', 'Lunch'), ('DINNER', 'Dinner'), ('SNACKS', 'snacks'), ('DESSERT', 'Dessert'), ('OTHER', 'Other')], max_length=10)),
            ],
        ),
    ]
