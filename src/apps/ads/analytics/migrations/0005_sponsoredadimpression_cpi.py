# Generated by Django 4.1.4 on 2022-12-26 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0004_searchadclicks_clicks_searchadclicks_cpc_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="sponsoredadimpression",
            name="cpi",
            field=models.IntegerField(null=True),
        ),
    ]
