from django import forms
from django.forms import ModelForm, CharField
from penjadwalan.models import *

class Fsuratijin(forms.ModelForm):
    class Meta:
        model   = Surat_ijin
        fields  = [
                    'judul',
                    'isi', 
                    'tgl_post',
                    'dokumen',
        ]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['pengirim'].widget.attrs.update({'readonly':'disabled'})
