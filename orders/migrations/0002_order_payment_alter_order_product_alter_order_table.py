# Generated by Django 4.1.6 on 2023-03-08 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_actice_product_active_and_more'),
        ('tables', '0001_initial'),
        ('payments', '0002_alter_payment_payment_type'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, db_column='pay_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.payment'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(blank=True, db_column='prod_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='table',
            field=models.ForeignKey(blank=True, db_column='tab_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.table'),
        ),
    ]
