# Generated by Django 2.0.2 on 2020-01-10 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penjadwalan', '0007_pengumuman'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengumuman',
            name='penerima',
            field=models.PositiveIntegerField(choices=[(1, 'GURU'), (2, 'SISWA')], default=1),
        ),
    ]
