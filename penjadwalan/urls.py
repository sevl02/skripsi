from django.contrib import admin
from . import views
from django.urls import path 


urlpatterns = [

    path('', views.data_guru, name='index'),
    # guru
    path('data_guru', views.data_guru, name='data_guru'),
    path('delete_guru/(^?P<id_delete>[0-9])', views.delete_guru, name='delete_guru' ),
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

]
 
 
