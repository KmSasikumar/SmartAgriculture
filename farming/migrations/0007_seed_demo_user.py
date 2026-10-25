import os

from django.contrib.auth.hashers import make_password
from django.db import migrations


def seed_demo_user(apps, schema_editor):
    # The live demo database resets on every deploy/restart (free host,
    # local SQLite file), so a migration that re-creates the demo account
    # whenever it is missing is what makes the demo login permanent.
    # The account is a plain user: no staff/superuser access, no admin.
    # Password comes from DEMO_PASSWORD when set, else the public demo
    # password shown on the sign-in page.
    # NOTE: historical models in migrations have no set_password() method,
    # so the hash is built with make_password() and assigned directly.
    User = apps.get_model("auth", "User")
    if not User.objects.filter(username="demo").exists():
        user = User(username="demo", email="demo@sams.demo", first_name="Demo", last_name="User")
        user.password = make_password(os.environ.get("DEMO_PASSWORD", "demo1234"))
        user.save()


def remove_demo_user(apps, schema_editor):
    apps.get_model("auth", "User").objects.filter(username="demo").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("farming", "0006_delete_loan_calculate"),
    ]

    operations = [
        migrations.RunPython(seed_demo_user, remove_demo_user),
    ]
