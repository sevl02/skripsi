from django.db import models
from django.utils import timezone
from .models import *
from django.contrib.auth.models import User, Group
# Create your models here.

HARI = (
    (1, 'SENIN'),
    (2, 'SELASA'),
    (3, 'RABU'),
    (4, 'KAMIS'),
    (5, 'JUMAT'),
    (6, 'SABTU')
)

JAMKE = (
    (1, '07.00'),
    (2, '07.40'),
    (3, '08.20'),
    (4, '09.00'),
    (5, '10.00'),
    (6, '10.20'),
    (7, '10.40'),
    (8, '11.20'),
    (9, '12.30'),
    (0, 'ISTIRAHAT'),
)
PENERIMA = (
    (1, 'GURU'),
    (2, 'SISWA'),
)
class Guru(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    nik         = models.CharField(unique=True, max_length=15)
    kode        = models.CharField(unique=True ,max_length=4)
    nama        = models.CharField(max_length=50)
    nama_blkg   = models.CharField(max_length=50)
    gelar       = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.nama)


# class Sks(models.Model):
#     kode_sks    = models.CharField(max_length=5)
#     jumlah_sks  = models.IntegerField(default=1)
    
#     def __str__(self):
#         return '{}'.format(self.jumlah_sks)

class Mapel(models.Model):
    kode_mapel  = models.CharField(max_length=10)
    nama        = models.CharField(max_length=50)
    # sks         = models.ForeignKey(Sks, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nama)

class Kelas(models.Model):
    kode_kelas    = models.CharField(max_length=10)
    kelas         = models.CharField(max_length=10)
    kapasitas     = models.IntegerField()
    keterangan    = models.TextField()

    def __str__(self):
        return '{}'.format(self.kelas)

# class Kelas(models.Model):
#     nama_kelas      = models.CharField(max_length=15)
#     ruang           = models.ForeignKey(Ruang, on_delete=models.CASCADE)
#     kode_jam        = models.CharField(max_length=5)
#     jam_pelajaran   = models.TimeField(auto_now_add=True, blank=True)

#     def __str__(self):
#         return '{}'.format(self.jam_pelajaran)
class Siswa(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    nis         = models.CharField(unique=True, max_length=15)
    nama        = models.CharField(max_length=50)
    nama_blkg   = models.CharField(max_length=50)
    kelas       = models.ForeignKey(Kelas, max_length=10, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.nis, self.nama)

class Hari(models.Model):
    kode_hari       = models.CharField(max_length=10)
    hari            = models.CharField(max_length=10)
 
    def __str__(self):
        return '{}'.format(self.hari)

# class Hari_has_jam(models.Model):
#     kode_jampel     = models.CharField(max_length=20)
#     hari            = models.ForeignKey(Hari, on_delete=models.CASCADE)
#     jam             = models.ForeignKey(Jam, on_delete=models.CASCADE)

#     def __str__(self):
#         return '{}'.format(self.kode_jampel)

class Penjadwalan(models.Model):
    kode_jadwal   = models.CharField(max_length=10)
    kelas         = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    hari          = models.PositiveIntegerField(default=1, choices= HARI)
    jamke         = models.PositiveIntegerField(default=1, choices= JAMKE)
    guru          = models.ForeignKey(Guru, on_delete=models.CASCADE)
    mapel         = models.ForeignKey(Mapel, on_delete=models.CASCADE)

    def __str__(self):
        return '{} | {}'.format(self.guru, self.mapel)

class Pengumuman(models.Model):
    penerima    = models.PositiveIntegerField(default=1, choices= PENERIMA)
    judul       = models.CharField(max_length=200)
    isi         = models.TextField()
    tgl_post    = models.DateTimeField(default=timezone.now)
    dokumen     = models.ImageField(upload_to = 'static/doc_pengumuman/', default = 'pic_folder/None/no-img.jpg')
    def __str__(self):
        return self.judul
    
class Surat_ijin(models.Model):
    pengirim    = models.CharField(max_length=200)
    judul       = models.CharField(max_length=200)
    isi         = models.TextField()
    tgl_post    = models.DateTimeField(default=timezone.now)
    dokumen     = models.ImageField(upload_to = 'static/doc_suratijin/', default = 'pic_folder/None/no-img.jpg')


    def __str__(self):
        return '{} {}'.format(self.pengirim, self.judul)

    
    
    
