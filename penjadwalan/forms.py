from django import forms
from .models import *

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