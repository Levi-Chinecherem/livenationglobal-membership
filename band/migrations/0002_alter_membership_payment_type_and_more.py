# Generated by Django 5.0.2 on 2024-02-29 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='payment_type',
            field=models.CharField(max_length=50),
        ),
        migrations.RemoveField(
            model_name='membershiptype',
            name='duration',
        ),
        migrations.AddField(
            model_name='membership',
            name='address',
            field=models.TextField(default='test address'),
        ),
        migrations.AddField(
            model_name='membership',
            name='city',
            field=models.CharField(default='test city', max_length=100),
        ),
        migrations.AddField(
            model_name='membership',
            name='country',
            field=models.CharField(default='test country', max_length=100),
        ),
        migrations.AddField(
            model_name='membership',
            name='state',
            field=models.CharField(default='test state', max_length=100),
        ),
        migrations.DeleteModel(
            name='CommonFields',
        ),
        migrations.DeleteModel(
            name='PaymentType',
        ),
    ]