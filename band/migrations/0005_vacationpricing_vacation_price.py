# Generated by Django 5.0.2 on 2024-03-04 08:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0004_autograph_generalmembership_vacation'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacationPricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Week 1', max_length=255)),
                ('price', models.DecimalField(decimal_places=0, default='1000', max_digits=8)),
            ],
            options={
                'verbose_name': 'Vacation Price',
                'verbose_name_plural': 'Vacation Prices',
            },
        ),
        migrations.AddField(
            model_name='vacation',
            name='price',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vacation_price', to='band.vacationpricing'),
            preserve_default=False,
        ),
    ]