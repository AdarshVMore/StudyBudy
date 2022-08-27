# Generated by Django 4.0.4 on 2022-08-27 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0013_remove_updateprofile_profilepic'),
    ]

    operations = [
        migrations.AddField(
            model_name='updateprofile',
            name='ProfilePic',
            field=models.ImageField(default=1, upload_to='post_images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='updateprofile',
            name='username',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
