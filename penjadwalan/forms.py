from django import forms
from .models import *

class Fpengumuman(forms.ModelForm):
    class Meta:
        model   = Pengumuman
        fields  = [ 'penerima',
                    'judul',
                    'isi',
                    'tgl_post',
                    'dokumen'
        ]
class Ftambahsiswa2(forms.ModelForm):        
    class Meta:
        model   = Siswa
        fields  = [
                    'user',
                    'nis',
                    'nama',
                    'nama_blkg',
                    'kelas',
                  ]   
                  
class Ftambahsiswa(forms.ModelForm):        
    class Meta:
        model   = Siswa
        fields  = [
                    'nis',
                    'nama',
                    'nama_blkg',
                    'kelas',
                  ]   
class Ftambahguru2(forms.ModelForm):        
    class Meta:
        model   = Guru
        fields  = [
                   'user',
                   'nik',
                   'kode',
                   'nama',
                   'nama_blkg', 
                   'gelar',
                  ]     
 
class Ftambahguru(forms.ModelForm):        
    class Meta:
        model   = Guru
        fields  = [
                   'nik',
                   'kode',
                   'nama',
                   'nama_blkg', 
                   'gelar',
                  ]     

class Ftambahmapel(forms.ModelForm):        
    class Meta:
        model   = Mapel
        fields  = [
                  'nama',
                  'kode_mapel',
                  ]
        # labels  = {
		# 	'sksFk':'Jumlah SKS',
		# }

class Ftambahkelas(forms.ModelForm):
    class Meta:
        model   = Kelas
        fields  = [
                  'kode_kelas',
                  'kelas',
                  'kapasitas',
                  'keterangan',
                  ]

class Ftambahjadwal(forms.ModelForm):
    class Meta:
        model   = Penjadwalan
        fields  = [
                    'kode_jadwal', 
                    'kelas',       
                    'hari',       
                    'jamke' ,      
                    'guru',       
                    'mapel',       
                  ]

class Ftambahjadwal2(forms.ModelForm):
    class Meta:
        model   = Penjadwalan
        fields  = [
                    'kode_jadwal', 
                    'kelas',       
                    'hari',       
                    'jamke',      
                    'guru',       
                    'mapel',       
                  ]
 
class LoginForm(forms.Form):
   user = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())