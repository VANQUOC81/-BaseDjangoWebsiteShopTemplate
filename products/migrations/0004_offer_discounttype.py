# Generated by Django 4.2 on 2023-05-07 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_offer_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='discountType',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
