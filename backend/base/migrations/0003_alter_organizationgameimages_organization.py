# Generated by Django 5.0.1 on 2024-02-14 10:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_organizationgameimages_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationgameimages',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.organizationlocation'),
        ),
    ]
