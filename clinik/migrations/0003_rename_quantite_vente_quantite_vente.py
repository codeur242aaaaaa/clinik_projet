# Generated by Django 4.2.6 on 2024-03-10 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinik', '0002_rename_nom_produit_designation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vente',
            old_name='quantite',
            new_name='quantite_vente',
        ),
    ]
