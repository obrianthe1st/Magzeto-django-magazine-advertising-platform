# Generated by Django 4.1.4 on 2022-12-10 23:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("category", "0001_initial"),
        ("article", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="tag",
            field=models.ManyToManyField(to="category.tag"),
        ),
    ]