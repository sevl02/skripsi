# Generated by Django 2.0.2 on 2020-01-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penjadwalan', '0012_auto_20200110_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengumuman',
            name='dokumen',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='static/doc_pengumuman/'),
        ),
    ]
