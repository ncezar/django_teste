# Generated by Django 2.0.6 on 2019-02-24 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0031_auto_20190223_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='preco_unitario',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_unit',
            field=models.FloatField(max_length=200),
        ),
    ]
