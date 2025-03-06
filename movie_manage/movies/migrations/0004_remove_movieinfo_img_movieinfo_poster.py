# Generated by Django 5.1.6 on 2025-03-05 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_movieinfo_img_movieinfo_year"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movieinfo",
            name="img",
        ),
        migrations.AddField(
            model_name="movieinfo",
            name="poster",
            field=models.ImageField(null=True, upload_to="images/"),
        ),
    ]
