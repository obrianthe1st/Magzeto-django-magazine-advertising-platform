# Generated by Django 4.1.4 on 2022-12-23 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="searchadclicks",
            options={
                "ordering": ("-created",),
                "verbose_name": "SearchAdClick",
                "verbose_name_plural": "SearchAdClicks",
            },
        ),
        migrations.AlterModelOptions(
            name="searchadimpression",
            options={
                "ordering": ("-created",),
                "verbose_name": "SearchAdImpression",
                "verbose_name_plural": "SearchAdImpressions",
            },
        ),
        migrations.AlterModelOptions(
            name="sponsoredadclicks",
            options={
                "ordering": ("-created",),
                "verbose_name": "SponsoredAdClick",
                "verbose_name_plural": "SponsoredAdClicks",
            },
        ),
        migrations.AlterModelOptions(
            name="sponsoredadimpression",
            options={
                "ordering": ("-created",),
                "verbose_name": "SponsoredAdImpression",
                "verbose_name_plural": "SponsoredAdImpressions",
            },
        ),
        migrations.RemoveField(
            model_name="searchadclicks",
            name="advertisement",
        ),
        migrations.RemoveField(
            model_name="searchadimpression",
            name="advertisement",
        ),
        migrations.RemoveField(
            model_name="sponsoredadclicks",
            name="advertisement",
        ),
        migrations.RemoveField(
            model_name="sponsoredadimpression",
            name="advertisement",
        ),
    ]
