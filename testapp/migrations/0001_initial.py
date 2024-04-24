# Generated by Django 5.0.3 on 2024-04-24 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("employee_no", models.IntegerField()),
                ("employee_name", models.CharField(max_length=250)),
                ("employee_salary", models.FloatField()),
                ("employee_address", models.CharField(max_length=300)),
            ],
        ),
    ]
