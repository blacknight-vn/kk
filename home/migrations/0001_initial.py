# Generated by Django 4.1.2 on 2022-10-07 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("image", models.ImageField(null=True, upload_to="folder1")),
                (
                    "image2",
                    models.FileField(blank=True, null=True, upload_to="folder1"),
                ),
            ],
        ),
    ]
