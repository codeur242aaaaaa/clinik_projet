# Generated by Django 4.2.6 on 2024-03-11 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinik', '0012_alter_rapportmensuel_mois'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapportmensuel',
            name='patients_consultes',
            field=models.IntegerField(default=0),
        ),
    ]
