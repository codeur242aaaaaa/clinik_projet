# Generated by Django 4.2.6 on 2024-03-10 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinik', '0004_vente_prix_unitaire'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vente',
            old_name='quantite_vente',
            new_name='quantite',
        ),
    ]