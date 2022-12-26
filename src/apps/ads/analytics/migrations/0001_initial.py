# Generated by Django 4.1.4 on 2022-12-23 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("advert", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SponsoredAdImpression",
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
                ("time_stamp", models.DateTimeField(auto_now_add=True)),
                ("sponsored_ad_id", models.IntegerField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "advertisement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="advert.sponsoredad",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SponsoredAdClicks",
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
                ("time_stamp", models.DateTimeField(auto_now_add=True)),
                ("sponsored_ad_id", models.IntegerField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "advertisement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="advert.sponsoredad",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SearchAdImpression",
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
                ("time_stamp", models.DateTimeField(auto_now_add=True)),
                ("searchad_id", models.IntegerField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "advertisement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="advert.searchad",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SearchAdClicks",
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
                ("time_stamp", models.DateTimeField(auto_now_add=True)),
                ("searchad_id", models.IntegerField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "advertisement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="advert.searchad",
                    ),
                ),
            ],
        ),
    ]