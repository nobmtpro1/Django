# Generated by Django 4.1 on 2022-09-09 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("src", "0003_userclient_has_courses_userclient_has_sessions"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userhassession",
            name="session",
        ),
        migrations.RemoveField(
            model_name="userhassession",
            name="user_client",
        ),
        migrations.DeleteModel(
            name="UserHasCourse",
        ),
        migrations.DeleteModel(
            name="UserHasSession",
        ),
    ]