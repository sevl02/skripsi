from django.contrib import admin
from . import views
from django.urls import path 


urlpatterns = [

    path('', views.data_guru, name='index'),
    
    # lain-lain 
    path('data_surat_ijin', views.data_surat_ijin, name='data_surat_ijin'),
    path('delete_surat_ijin/(^?P<id_delete>[0-9])', views.delete_surat_ijin, name='delete_surat_ijin' ),

    # path('update-surat-ijin', views.data_surat_ijin, name='data_surat_ijin'),
    path('data_pengumuman', views.data_pengumuman, name='data_pengumuman'),
    path('tambah_pengumuman', views.tambah_pengumuman, name='tambah_pengumuman'),
    path('update_pengumuman/<int:id_update>', views.update_pengumuman, name='update_pengumuman'),
    path('delete_pengumuman/(^?P<id_delete>[0-9])', views.delete_pengumuman, name='delete_pengumuman' ),


    # siswa
    path('data_siswa/', views.data_siswa, name='data_siswa'),
    path('siswa_selected_kelas/<int:kelas_id>', views.siswa_selected_kelas, name='siswa_selected_kelas' ),
    path('update_siswa/<int:id_update>', views.update_siswa, name='update_siswa'),
    path('delete_siswa/(^?P<username>)', views.delete_siswa, name='delete_siswa' ),


    # guru
    path('data_guru', views.data_guru, name='data_guru'),
    path('delete_guru/(^?P<username>)', views.delete_guru, name='delete_guru' ),
    path('jml_pel/<int:id_guru>', views.jml_pel, name='jml_pel'),
    path('update_guru/<int:id_update>', views.update_guru, name='update_guru'),
    path('tambah_guru', views.tambah_guru, name='tambah_guru'),
    # mapel
    path('data_mapel', views.data_mapel, name='data_mapel'),
    path('update_mapel/<int:id_update>', views.update_mapel, name='update_mapel'),
    path('tambah_mapel', views.tambah_mapel, name='tambah_mapel'),
    path('delete_mapel/(^?P<id_delete>[0-9])', views.delete_mapel, name='delete_mapel' ),
    # ruang kelas
    path('data_kelas', views.data_kelas, name='data_kelas'),
    path('tambah_kelas', views.tambah_kelas, name='tambah_kelas'),
    path('delete_kelas/(^?P<id_delete>[0-9])', views.delete_kelas, name='delete_kelas' ),
    path('update_kelas/<int:id_update>', views.update_kelas, name='update_kelas'),
    # jam pelajaran
    path('data_jampel', views.data_jampel, name='data_jampel'),
    path('tambah_jampel', views.tambah_jampel, name='tambah_jampel'),
    path('delete_jampel/(^?P<id_delete>[0-9])', views.delete_jampel, name='delete_jampel' ),
    path('update_jampel/<int:id_update>', views.update_jampel, name='update_jampel'),
    # JADWAL
    path('jadwal/', views.kelas_dropdown, name='data_jadwal'),
    path('jadwal/<int:kelas_id>', views.semuaJadwal, name='jadwal'),
    path('update_jadwal/<int:kelas>/<int:hari>/<int:jamke>', views.update_jadwal, name='update_jadwal'),
    path('tambah_jadwal/<int:kelas>/<int:hari>/<int:jamke>', views.tambah_jadwal, name='tambah_jadwal'),
    path('tambah_jadwal2', views.tambah_jadwal2, name='tambah_jadwal2'),
    path('delete_jadwal/(^?P<id_delete>[0-9])', views.delete_jadwal, name='delete_jadwal' ),
]
 
 
