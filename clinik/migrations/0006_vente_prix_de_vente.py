# Generated by Django 4.2.6 on 2024-03-11 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinik', '0005_rename_quantite_vente_vente_quantite'),
    ]

    operations = [
        migrations.AddField(
            model_name='vente',
            name='prix_de_vente',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
