# Generated by Django 3.2.16 on 2022-11-15 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0223_voucher_min_usages'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceaddress',
            name='invoice_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
