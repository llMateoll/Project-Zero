# Generated by Django 3.0.8 on 2021-01-12 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201229_1308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='profile',
            name='money',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=30),
        ),
    ]
