<<<<<<< HEAD
# Generated by Django 3.1.3 on 2021-01-16 19:29
=======
# Generated by Django 3.1.5 on 2021-01-15 03:55
>>>>>>> a9da69bc600b831165ada616637a5efd2d816871

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
            ],
        ),
    ]
