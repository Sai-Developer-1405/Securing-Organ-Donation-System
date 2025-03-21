# Generated by Django 5.0.5 on 2024-05-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hospital",
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
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Hospital Name"),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("phone", models.CharField(max_length=15, verbose_name="Phone Number")),
                ("password", models.CharField(max_length=128, verbose_name="Password")),
                ("address", models.TextField(verbose_name="Address")),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="hospital_images/",
                        verbose_name="Hospital Image",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Approved", "Approved"),
                            ("Rejected", "Rejected"),
                        ],
                        default="Pending",
                        max_length=10,
                        verbose_name="Approval Status",
                    ),
                ),
            ],
        ),
    ]
