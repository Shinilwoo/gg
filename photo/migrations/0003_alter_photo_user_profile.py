# Generated by Django 4.2.6 on 2023-12-03 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [

        ('photo', '0002_photo_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile'),
        ),
    ]
