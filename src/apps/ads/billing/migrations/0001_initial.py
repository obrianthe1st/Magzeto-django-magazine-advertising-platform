# Generated by Django 4.1.4 on 2022-12-21 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Billing",
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
                ("card_holder_name", models.CharField(max_length=150)),
                ("card_number", models.CharField(max_length=16)),
                (
                    "country",
                    models.CharField(
                        choices=[
                            ("USA", "USA"),
                            ("Jamaica", "Jamaica"),
                            ("Canada", "Canada"),
                            ("Bahamas", "Bahamas"),
                            ("Cayman", "Cayman"),
                            ("India", "India"),
                        ],
                        default="USA",
                        max_length=20,
                    ),
                ),
                ("month", models.CharField(max_length=2)),
                ("day", models.CharField(max_length=2)),
                ("cvc", models.CharField(max_length=3)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "card_holder",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "billing",
                "verbose_name_plural": "billings",
                "ordering": ["-created"],
            },
        ),
    ]
