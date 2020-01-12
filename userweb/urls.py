from django.urls import path, include
from userweb import views

app_name = 'userweb'
urlpatterns = [
    path('', views.index, name='index'),
    path('base', views.base, name='base'),
    path('kirim_surat_ijin', views.kirim_surat_ijin, name='kirim_surat_ijin'),
    path('user_pengumuman/', views.user_pengumuman, name='user_pengumuman'),
    #jadwal
    path('jadwal/', views.kelas_dropdown, name='data_jadwal'),
    path('jadwal/<int:kelas_id>', views.semuaJadwal, name='jadwal'),

]