# Generated by Django 2.2 on 2019-09-15 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customsclear', '0003_auto_20190909_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about',
            field=models.TextField(max_length=1000),
        ),
    ]
