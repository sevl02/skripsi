from django.contrib import admin
from .models import Mapel, Guru, Penjadwalan, Kelas, Siswa, Surat_ijin, Pengumuman

# Register your models here.

admin.site.register(Kelas)
admin.site.register(Mapel)
admin.site.register(Guru)
admin.site.register(Siswa)
admin.site.register(Penjadwalan)
admin.site.register(Pengumuman)
admin.site.register(Surat_ijin)
