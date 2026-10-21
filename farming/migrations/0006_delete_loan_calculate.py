# Generated for the debug cycle: loan_calculate existed only in migration
# state (removed from models.py long ago), so every fresh database grew a
# stray farming_loan_calculate table and makemigrations --check failed.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farming', '0005_float_fields_for_calculators'),
    ]

    operations = [
        migrations.DeleteModel(
            name='loan_calculate',
        ),
    ]
