# Generated by Django 2.0.2 on 2020-01-10 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penjadwalan', '0009_surat_ijin_dokumen'),
    ]

    operations = [
        migrations.AddField(
            model_name='pengumuman',
            name='dokumen',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='static/doc_pengumuman/'),
        ),
        migrations.AlterField(
            model_name='surat_ijin',
            name='dokumen',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='static/doc_suratijin/'),
        ),
    ]
