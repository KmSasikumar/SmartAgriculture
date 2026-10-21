# Generated for the debug cycle: calculator inputs/results are fractional
# (e.g. yield 100.75 kg/acre); IntegerField truncated them and rejected
# decimal input outright.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farming', '0004_remove_loan_calculate_profit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculate_yeild',
            name='area',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='calculate_yeild',
            name='result',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='calculate_yeild',
            name='weigth',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='crop_productions',
            name='crop_yeild',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='crop_productions',
            name='land_acer',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='crop_productions',
            name='market_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='crop_productions',
            name='profit',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='crop_productions',
            name='totalCost',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='crop_productions',
            name='totalProduction',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='crop_productions',
            name='totalRevenue',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='crop_productions',
            name='user_cost',
            field=models.FloatField(),
        ),
    ]
