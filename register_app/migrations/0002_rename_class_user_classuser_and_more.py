# Generated by Django 5.0.6 on 2024-06-22 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("register_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Class_user",
            new_name="ClassUser",
        ),
        migrations.RenameModel(
            old_name="Region_user",
            new_name="RegionUser",
        ),
        migrations.RenameModel(
            old_name="User_information",
            new_name="UserInformation",
        ),
    ]
