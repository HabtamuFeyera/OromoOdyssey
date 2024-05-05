# Generated by Django 5.0.3 on 2024-05-05 11:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Attraction",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("location", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="attraction_images/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]