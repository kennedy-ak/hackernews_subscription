# Generated by Django 5.1.1 on 2024-11-15 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscriber",
            name="name",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="subscriber",
            name="number",
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]