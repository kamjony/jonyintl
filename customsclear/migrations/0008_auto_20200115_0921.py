# Generated by Django 3.0.2 on 2020-01-15 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customsclear', '0007_auto_20200113_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_name', models.CharField(max_length=50)),
                ('gallery_image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
    ]
