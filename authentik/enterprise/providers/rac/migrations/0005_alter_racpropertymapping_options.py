# Generated by Django 5.0.8 on 2024-08-12 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_providers_rac", "0004_alter_connectiontoken_expires"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="racpropertymapping",
            options={
                "verbose_name": "RAC Provider Property Mapping",
                "verbose_name_plural": "RAC Provider Property Mappings",
            },
        ),
    ]
