from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from penjadwalan.models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count

# Create your views here.

def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    
    def in_group(u):
        return u.is_active and (u.is_superuser or bool(u.groups.filter(name__in=group_names)))
    return user_passes_test(in_group)
    
@group_required('students', 'teachers')
def index(request):
    
    # memunculkan context jumlah jam ajar pada guru
    for i in Guru.objects.filter(user=request.user):
        if i.user == request.user:
            idguru_login = i.id
            # print(i.id)
            list_mapel = Penjadwalan.objects.filter(guru=idguru_login)
            jam_ajar = len(list_mapel)

            context= {
                        "jam_ajar" :  "Total {} jam ajar".format(jam_ajar),
            }  
    
            return render(request, 'userweb/index.html', context)
    return render(request, 'userweb/index.html')


@login_required
def user_pengumuman(request):
    for i in User.objects.filter(groups=1):
        if i == request.user:
            mpengumuman = Pengumuman.objects.filter(penerima=2)
        else:
            mpengumuman = Pengumuman.objects.filter(penerima=1)

    context = {
                    "data"  : mpengumuman,
                    "title" : "Pengumuman",
        }
    return render(request, 'userweb/user_pengumuman.html', context)

@login_required
def kirim_surat_ijin(request):
    data_pengirim = User.objects.get(username=request.user)
    print("print user:", data_pengirim.username) #guru2
    add_form = Fsuratijin(request.POST or None)
    # data = {
    #     'pengirim' : data_pengirim,
    # }

    # add_form = Fsuratijin(request.POST or None, initial=data, instance=data_pengirim)

    if request.method == 'POST':
        if add_form.is_valid():
            pengirim    = data_pengirim.username
            judul       = add_form.cleaned_data['judul']
            isi         = add_form.cleaned_data['isi'] 
            tgl_post    = add_form.cleaned_data['tgl_post']
            dokumen     = add_form.cleaned_data['dokumen']
            add_form   = Surat_ijin(pengirim=pengirim, judul=judul, isi=isi, tgl_post=tgl_post, dokumen=dokumen)

            add_form.save()
            print ("INPUT !!!!")
        return redirect('userweb:kirim_surat_ijin')
    
    context = {
        'add_form'  : add_form,
        "title"     : "Kirim Surat Ijin",
    }
    return render(request, 'userweb/kirim_surat_ijin.html', context)


# def user_pengumuman(request,i):
#     mpengumuman = Pengumuman.objects.filter(penerima=i)
#     def in_group(u):
#         if u.groups__name == "students" :
#             i=1
#         else:
#             i=2
#     print(user)
#     context = {
#                 'grup'  : i,
#                 "data"  : mpengumuman,
#                 "title" : "Pengumuman",
#     }
#     return render(request, 'userweb/user_pengumuman.html', context)
    
def base(request):
    return render(request, 'userweb/base.html')


########## jadwal ############
@login_required
def kelas_dropdown(request):
    # kelas_id = request.GET.get('kelas')
    mkelas = Kelas.objects.all().order_by('kelas')
    print(mkelas)
    context = {
                "data" : mkelas,
                }
    template = 'userweb/user_lihat_jadwal.html'
    return render (request, template, context)    

@login_required
def semuaJadwal(request,kelas_id):
 
    hari = [1, 2, 3, 4, 5, 6]
    jam = [1, 2, 3, 4, 5, 6, 7, 8]
    kelas = Kelas.objects.all().order_by('kelas')
    kelas_saat_ini = Kelas.objects.filter(id = kelas_id)
    jadwal = Penjadwalan.objects.filter(kelas = kelas_id)
    list_jadwal = []
    for i in jam:
        for x in hari:
            jadwalku = jadwal.filter(jamke=i,hari=x)
            if jadwalku:
                for y in jadwalku:
                    if y.hari == 1:
                        if y.jamke == i:
                            mapel_senin = y.mapel
                        else:
                            mapel_senin = '-'
                    if y.hari == 2:
                        if y.jamke == i:
                            mapel_selasa = y.mapel
                        else:
                            mapel_selasa = '-'
                    if y.hari == 3:
                        if y.jamke == i:
                            mapel_rabu = y.mapel
                        else:
                            mapel_rabu = '-'
                    if y.hari == 4:
                        if y.jamke == i:
                            mapel_kamis = y.mapel
                        else:
                            mapel_kamis = '-'
                    if y.hari == 5:
                        if y.jamke == i:
                            mapel_jumat = y.mapel
                        else:
                            mapel_jumat = '-'
                    if y.hari == 6:
                        if y.jamke == i:
                            mapel_sabtu = y.mapel
                        else:
                            mapel_sabtu = '-'
            else:
                if x == 1:
                    mapel_senin = '-'
                if x == 2:
                    mapel_selasa = '-'
                if x == 3:
                    mapel_rabu = '-'
                if x == 4:
                    mapel_kamis = '-'
                if x == 5: 
                    mapel_jumat = '-'
                if x == 6:
                    mapel_sabtu = '-'
    # url = request.build_absolute_uri
    # split_url = url.split("/")[-3:]
    # list_url = []
    # for i in split_url:
    #     list_url = list_url.append(i)
    #     return list_url

        list_jadwal.append({
            "mapel_senin"   : mapel_senin,
            "mapel_selasa"  : mapel_selasa,
            "mapel_rabu"    : mapel_rabu,
            "mapel_kamis"   : mapel_kamis,
            "mapel_jumat"   : mapel_jumat,
            "mapel_sabtu"   : mapel_sabtu,
            "kelas"         : kelas_id,
      
            

        })
    # print(list_jadwal)
    
    context = {
        "senin"     : mapel_senin,
        "selasa"    : mapel_selasa, 
        "rabu"      : mapel_rabu,
        "kamis"     : mapel_kamis,
        "jumat"     : mapel_jumat,
        "sabtu"     : mapel_sabtu,
        "jadwal"    : list_jadwal,
        "data"      : kelas,
        "kelas_saat_ini" : kelas_saat_ini, 
        "title"     : "Jadwal Pelajaran"
    }
    
    template = 'userweb/user_lihat_jadwal.html'
    return render (request, template, context)

