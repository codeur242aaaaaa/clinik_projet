# Generated by Django 4.2.6 on 2024-03-11 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinik', '0013_alter_rapportmensuel_patients_consultes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapportmensuel',
            name='patients_examines',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rapportmensuel',
            name='patients_hospitalises',
            field=models.IntegerField(default=0),
        ),
    ]
