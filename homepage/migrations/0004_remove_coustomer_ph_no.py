# Generated by Django 4.2.13 on 2024-07-05 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0003_alter_coustomer_ph_no"),
    ]

    operations = [
        migrations.RemoveField(model_name="coustomer", name="ph_no",),
    ]
