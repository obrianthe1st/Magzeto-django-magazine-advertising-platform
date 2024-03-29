# Generated by Django 4.1.4 on 2023-01-02 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0009_alter_searchadclicks_time_stamp_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="searchadclicks",
            name="clicks",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="searchadimpression",
            name="impressions",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="sponsoredadclicks",
            name="clicks",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="sponsoredadimpression",
            name="impressions",
            field=models.IntegerField(default=0, null=True),
        ),
    ]
