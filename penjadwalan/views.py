from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib import messages 
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count
# Create your views here.


############ lain-lain #############
def data_surat_ijin(request):

    msuratijin = Surat_ijin.objects.all()
    

    context={"data"     :  msuratijin, 
            "title"     : "Surat Ijin",
            }
    return render(request, 'penjadwalan/surat_ijin.html', context)

def delete_surat_ijin(request, id_delete):
    Surat_ijin.objects.filter(id=id_delete).delete()
    return redirect('data_surat_ijin')


def data_pengumuman(request):
    mpengumuman = Pengumuman.objects.all()

    context={"data"     :  mpengumuman, 
            "title"     : "Pengumuman",
            }
    return render(request, 'penjadwalan/pengumuman.html', context)

def delete_pengumuman(request, id_delete):
    Pengumuman.objects.filter(id=id_delete).delete()
    return redirect('data_pengumuman')

def tambah_pengumuman(request):
    add_form = Fpengumuman(request.POST or None)
    if request.method == 'POST':
    
        if add_form.is_valid():
           add_form.save()
           print ("INPUT !!!!")

        return redirect('data_pengumuman')
    context = {
        'add_form': add_form,
    }
    return render(request, 'penjadwalan/tambah_pengumuman.html', context )

def update_pengumuman(request, id_update):
    pengumuman_update = Pengumuman.objects.get(id=id_update)
    data = {
        'judul'         : pengumuman_update.judul,
        'isi'           : pengumuman_update.isi,
        'tgl_post'      : pengumuman_update.tgl_post,
    }
    add_form = Fpengumuman(request.POST or None, initial=data, instance=pengumuman_update)
    
    if request.method == 'POST':
        if add_form.is_valid():
           add_form.save()
           print ("save!!!!")
        else:
            print (add_form.errors)

        return redirect('data_pengumuman')
 
    context = {
        'add_form': add_form, 
    }
    return render(request, 'penjadwalan/tambah_pengumuman.html', context )



############ sign up user #############

def signup_siswa(request):
    if request.method == 'POST':
        userform = UserCreationForm(request.POST)
        siswaform = Ftambahsiswa(request.POST or None)

        if userform.is_valid():
            print("tersave")
            userform.save()
            print("tersave2")

            username = userform.cleaned_data.get('username')
            siswa_userform = User.objects.get(username = username)
            # raw_password = userform.cleaned_data.get('password1')
            
            if request.method == "POST" and siswaform.is_valid():
                print("valid guruform")
                # print('tes', guru_userform.id)
                # guruform.user = guru_userform.id
                user_id     = siswa_userform.id
                nis         = siswaform.cleaned_data['nis']
                nama        = siswaform.cleaned_data['nama'] 
                nama_blkg   = siswaform.cleaned_data['nama_blkg']
                kelas       = siswaform.cleaned_data['kelas']
                my_group = Group.objects.get(name='students') 
                my_group.user_set.add(user_id)
                
                siswaform   = Siswa(user_id=user_id, nis=nis, nama=nama, nama_blkg=nama_blkg, kelas=kelas)
                # formfinal.save()
                siswaform.save()

                print("data siswa masok")

                user = authenticate(username=username, password=username)
                login(request, user)
                return redirect('data_siswa')

    else:
        userform    = UserCreationForm()
        siswaform   = Ftambahsiswa()
    context = {
            'userform'  : userform,
            'siswaform' : siswaform,

    }
    return render(request, 'registration/signup_siswa.html', context)


def signup(request):
    if request.method == 'POST':
        userform = UserCreationForm(request.POST)
        guruform = Ftambahguru(request.POST or None)

        if userform.is_valid():
            print("tersave")
            userform.save()
            print("tersave2")

            username = userform.cleaned_data.get('username')
            guru_userform = User.objects.get(username = username)
            # raw_password = userform.cleaned_data.get('password1')
            
            if request.method == "POST" and guruform.is_valid():
                print("valid guruform")
                # print('tes', guru_userform.id)
                # guruform.user = guru_userform.id
                user_id     = guru_userform.id
                nik         = guruform.cleaned_data['nik']
                kode        = guruform.cleaned_data['kode'] 
                nama        = guruform.cleaned_data['nama']
                nama_blkg   = guruform.cleaned_data['nama_blkg']
                gelar       = guruform.cleaned_data['gelar']
                my_group = Group.objects.get(name='teachers') 
                my_group.user_set.add(user_id)
                
                guruform   = Guru(user_id=user_id, nik=nik, kode=kode, nama=nama, nama_blkg=nama_blkg, gelar=gelar)
                # formfinal.save()
                guruform.save()

                print("data guru masok")

                user = authenticate(username=username, password=username)
                login(request, user)
                return redirect('data_guru')

    else:
        userform = UserCreationForm()
        guruform = Ftambahguru()
    context = {
            'userform': userform,
            'guruform': guruform,

    }
    return render(request, 'registration/signup.html', context)


def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    # def in_groups(u):
    #     if u.is_authenticated():
    #         if bool(u.groups.filter(name__in=group_names)):
    #             return True
    #     return False

    # return user_passes_test(in_groups, login_url='403')
    def in_group(u):
        return u.is_active and (u.is_superuser or bool(u.groups.filter(name__in=group_names)))
    return user_passes_test(in_group)
    
@group_required('students', 'teachers')
def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if request.user.groups.filter(name="students").exists():
        # user is an admin
        print("berhasil masuk index user")
        return redirect("generalweb:index")
    if request.user.groups.filter(name="teachers").exists():
        # user is an admin
        print("berhasil masuk index guru")
        return redirect("generalweb:index")
    else:
        print("masuk admin")
        return redirect("index")

############ base #############
@user_passes_test(lambda u: u.is_superuser)
def base(request):
    return render(request, 'penjadwalan/base.html')
@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'penjadwalan/index.html')

@user_passes_test(lambda u: u.is_superuser)
def data_tables(request):
    return render(request, 'penjadwalan/tables-data.html', context)

############ siswa #############
@user_passes_test(lambda u: u.is_superuser)

def siswa_selected_kelas(request, kelas_id):
    mkelas = Kelas.objects.all().order_by('kelas')
    msiswa = Siswa.objects.filter(kelas = kelas_id)
    kelas_selected = Kelas.objects.filter(id = kelas_id)
    print(msiswa)

    print(mkelas)
    context = {
                "kelas_selected" : kelas_selected,
                "data"  : msiswa,
                "kelas" : mkelas,
                "title" : "Siswa",
                }
    return render (request, "penjadwalan/data_siswa.html", context)

@user_passes_test(lambda u: u.is_superuser)
def data_siswa(request):

    kelas_selected = " "
    mkelas  = Kelas.objects.all().order_by('kelas')
    msiswa = Siswa.objects.all()
    

    context={
            "kelas_selected" : kelas_selected,
            "data"     : msiswa, 
            "kelas"     : mkelas,
            "title"     : "Siswa",
            "kelas_saat_ini" : kelas_siswa,
            }
    return render(request, 'penjadwalan/data_siswa.html', context)



def update_siswa(request, id_update):
    siswa_update = Siswa.objects.get(id=id_update)
    data = {
        'user'          : siswa_update.user,
        'nis'           : siswa_update.nis,
        'nama'          : siswa_update.nama,
        'nama_blkg'     : siswa_update.nama_blkg,
        'kelas'         : siswa_update.kelas,
    }
    add_form = Ftambahsiswa2(request.POST or None, initial=data, instance=siswa_update)
    
    if request.method == 'POST':
        if add_form.is_valid():
           add_form.save()
           print ("save!!!!")
        else:
            print (add_form.errors)

        return redirect('data_siswa')
 
    context = {
        'add_form': add_form,
    }
    return render(request, 'penjadwalan/tambah_siswa.html', context )

def delete_siswa(request, username):
    User.objects.filter(username=username).delete()
    return redirect('data_siswa')

############ guru #############
@user_passes_test(lambda u: u.is_superuser)
def data_guru(request):
    
    mguru = Guru.objects.all()
    mjadwal = Penjadwalan.objects.all()
    mapel = Penjadwalan.objects.values('guru').annotate(Count('mapel'))
    # join1 = Penjadwalan.objects.selected_related('guru')
    list_data=[]
    # print(mapel)
    # for i in mapel:
    #     # print(i.get('guru'))
    #     list_data = []
    #     guru = Guru.objects.filter(id=i.get('guru'))
    #     print('kkkkkkkkkkkk',guru)
    #     for x in guru:
    #         jumlah_jam = i.get('mapel__count')
    #         nama_guru = x.nama
    #         id_guru = x.id
    #         print(nama_guru,"jml jam",jumlah_jam )
    # ====================================================
    # for i in mguru:
    #     print(i.id)
    #     idguru = i.id
    #     for j in mjadwal:
    #         print(j.guru)
    #         if j.guru == idguru:
    #             jumlah_mapel = Penjadwalan.objects.values('j.guru').annotate(Count('j.mapel'))
    #             print(jumlah_mapel)
    #             namaguru = i.nama
    #             # jumlah_jam = Count(j.mapel)

        # list_data.append({
        #                 "nama_guru"  : nama_guru,
        #                 "jumlah_jam" : jumlah_jam,
        #                 "id"          : id_guru,
        # })

    for i in mguru:
        idguru = i.id
        panggil_guru = Penjadwalan.objects.filter(guru=idguru)
        # print(idguru)
        # print(panggil_guru)
        for j in panggil_guru:
            print(j.mapel, i.nama) 
    # print(list_data)

    context={"data"     :  mguru, 
            "title"     : "Guru",

            }
    return render(request, 'penjadwalan/data_guru.html', context)

def jml_pel(request, id_guru):
    mapel = Penjadwalan.objects.values('guru').annotate(Count('mapel'))

    print('grup by', mapel)
    context = {
        "mapel" : mapel,
    }
    return render(request, 'penjadwalan/data_guru.html', context)

def tambah_guru(request):
    add_form = Ftambahguru(request.POST or None)
    if request.method == 'POST':
       
    
        if add_form.is_valid():
           add_form.save()
           print ("INPUT !!!!")

        return redirect('data_guru')
    context = {
        'add_form': add_form,
    }
    return render(request, 'penjadwalan/tambah_guru.html', context )

def delete_guru(request, username):
    User.objects.filter(username=username).delete() #username karena mau apus usernya cascade 
    return redirect('data_guru')

def update_guru(request, id_update):
    guru_update = Guru.objects.get(id=id_update)
    data = {
        'user'          : guru_update.user,
        'nik'           : guru_update.nik,
        'kode'          : guru_update.kode,
        'nama'          : guru_update.nama,
        'nama_blkg'     : guru_update.nama_blkg,
        'gelar'         : guru_update.gelar,
    }
    add_form = Ftambahguru2(request.POST or None, initial=data, instance=guru_update)
    
    if request.method == 'POST':
        if add_form.is_valid():
           add_form.save()
           print ("save!!!!")
        else:
            print (add_form.errors)

        return redirect('data_guru')
 
    context = {
        'add_form': add_form,
    }
    return render(request, 'penjadwalan/tambah_guru.html', context )

############ Kelas #############

def data_kelas(request):
    
    mkelas = Kelas.objects.all()

    context={"data"     :  mkelas, 
            "title"     : "Kelas",
            }
    return render(request, 'penjadwalan/data_kelas.html', context)

def tambah_kelas(request):
    add_form = Ftambahkelas(request.POST or None)
    if request.method == 'POST':
        if add_form.is_valid():
           add_form.save()
           print ("INPUT !!!!")

        return redirect('data_kelas')
    context = {
        'add_form'  : add_form,
    }
    return render(request, 'penjadwalan/tambah_kelas.html', context )

def update_kelas(request, id_update):
    kelas_update = Kelas.objects.get(id=id_update)
    data = {
        'kode_kode_kelas': kelas_update.kode_kelas,
        'kelas  '        : kelas_update.kelas,
        'kapasitas'      : kelas_update.kapasitas,
        'keterangan'     : kelas_update.keterangan,
        
    }
    add_form = Ftambahkelas(request.POST or None, initial=data, instance=kelas_update)
    
    if request.method == 'POST':
        if add_form.is_valid():
           add_form.save()
           print ("save!!!!")
        else:
            print (add_form.errors)

        return redirect('data_kelas')
 
    context = {
        'add_form': add_form,
    }
    return render(request, 'penjadwalan/tambah_kelas.html', context )


def delete_kelas(request, id_delete):
    Kelas.objects.filter(id=id_delete).delete()
    return redirect('data_kelas')


############ mata pelajaran #############

def data_mapel(request):
    mmapel = Mapel.objects.all()
    print(mmapel)
    context={"data" :  mmapel,
            "title" : 'Mata Pelajaran',
            }
    return render(request, 'penjadwalan/data_mapel.html', context)

def tambah_mapel(request):
    add_form = Ftambahmapel(request.POST or None)
    if request.method == 'POST':
        if add_form.is_valid():
           add_form.save()
           print ("INPUT !!!!")

        return redirect('data_mapel')
    context = {
        'add_form': add_form,
    }
    return render(request, 'penjadwalan/tambah_mapel.html', context )   

def update_mapel(request, id_update):

    mapel_update = Mapel.objects.get(id=id_update)

    data = {
        'kode'          : mapel_update.kode_mapel,
        'nama'          : mapel_update.nama,
        'sksFk'         : mapel_update.sksFk_id,

    }
    add_form = Ftambahmapel(request.POST or None, initial=data, instance=mapel_update)
    
    if request.method == 'POST':
        if add_form.is_valid():
           add_form.save()
           print ("save!!!!")
        else:
            print (add_form.errors)

        return redirect('data_mapel')
 
    context = {
        'add_form': add_form,
    }
    return render(request, 'penjadwalan/tambah_mapel.html', context )

def delete_mapel(request, id_delete):
    Mapel.objects.filter(id=id_delete).delete()
    return redirect('data_mapel')

########## jampel ############

def data_jampel(request):
    mjampel = Hari_has_jam.objects.all()
    context={"data"     :  mjampel,
            "title"     : 'Jam Pelajaran',
            }
    return render(request, 'penjadwalan/data_jampel.html', context)

def tambah_jampel(request):
    add_form = Ftambahjampel(request.POST or None)
    if request.method == 'POST':
        if add_form.is_valid():
           add_form.save()
           print ("INPUT !!!!")

        return redirect('data_jampel')
    context = {
        'add_form': add_form,
    }
    return render(request, 'penjadwalan/tambah_jampel.html', context ) 

def update_jampel(request, id_update):

    jampel_update = Hari_has_jam.objects.get(id=id_update)

    data = {
        'kode_jampel'   : jampel_update.kode_jampel,
        'hariFk'        : jampel_update.hariFk,
        'jamFk'         : jampel_update.jamFk,

    }
    add_form = Ftambahjampel(request.POST or None, initial=data, instance=jampel_update)
    
    if request.method == 'POST':
        if add_form.is_valid():
           add_form.save()
           print ("save!!!!")
        else:
            print (add_form.errors)

        return redirect('data_jampel')
 
    context = {
        'add_form': add_form,
    }
    return render(request, 'penjadwalan/tambah_jampel.html', context )

def delete_jampel(request, id_delete):
    Hari_has_jam.objects.filter(id=id_delete).delete()
    return redirect('data_jampel')


########## jadwal ############
def kelas_dropdown(request):
    # kelas_id = request.GET.get('kelas')
    mkelas = Kelas.objects.all().order_by('kelas')
    print(mkelas)
    context = {
                "data" : mkelas,
                }
    return render (request, "penjadwalan/data_jadwal.html", context)
        

def semuaJadwal(request,kelas_id):
    hari = [1, 2, 3, 4, 5, 6]
    jam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    kelas = Kelas.objects.all().order_by('kelas')
    kelas_saat_ini = Kelas.objects.filter(id = kelas_id)
    jadwal = Penjadwalan.objects.filter(kelas = kelas_id)

    for i in jadwal:
        print("print id jadwal", i.id)
        id_jadwal_ku = i.id

    # mguru = Guru.objects.filter(id)
    list_jadwal = []
    for i in jam:
        for x in hari:
            jadwalku = jadwal.filter(jamke=i,hari=x)
            if jadwalku:
                for y in jadwalku:
                    if y.hari == 1:
                        if y.jamke == i:
                            mapel_senin = y.mapel
                            guru_senin  = y.guru
                            id_senin    = y.id
                        else:
                            mapel_senin = '-'
                            guru_senin  = ' '
                            id_senin    = 0
                    if y.hari == 2:
                        if y.jamke == i:
                            mapel_selasa = y.mapel
                            guru_selasa  = y.guru
                            id_selasa      = y.id
                        else:
                            mapel_selasa = '-'
                            guru_selasa  = ' '
                            id_selasa    = 0
                    if y.hari == 3:
                        if y.jamke == i:
                            mapel_rabu = y.mapel
                            guru_rabu  = y.guru
                            id_rabu    = y.id
                        else:
                            mapel_rabu = '-'
                            guru_rabu  = ' '
                            id_rabu    = 0
                    if y.hari == 4:
                        if y.jamke == i:
                            mapel_kamis = y.mapel
                            guru_kamis  = y.guru
                            id_kamis    = y.id
                        else:
                            mapel_kamis = '-'
                            guru_kamis  = ' '
                            id_kamis    = 0
                    if y.hari == 5:
                        if y.jamke == i:
                            mapel_jumat = y.mapel
                            guru_jumat  = y.guru
                            id_jumat    = y.id
                        else:
                            mapel_jumat = '-'
                            guru_jumat  = ' '
                            id_jumat    = 0
                    if y.hari == 6:
                        if y.jamke == i:
                            mapel_sabtu = y.mapel
                            guru_sabtu  = y.guru
                            id_sabtu    = y.id
                        else:
                            mapel_sabtu = '-'
                            guru_sabtu  = ' '
                            id_sabtu    = 0
            else:
                if x == 1:
                    mapel_senin = '-'
                    guru_senin  = ' '
                    id_senin    = 0
                if x == 2:
                    mapel_selasa = '-'
                    guru_selasa  = ' '
                    id_selasa    = 0
                if x == 3:
                    mapel_rabu = '-'
                    guru_rabu  = ' '
                    id_rabu    = 0
                if x == 4:
                    mapel_kamis = '-'
                    guru_kamis = ' '
                    id_kamis    = 0
                if x == 5: 
                    mapel_jumat = '-'
                    guru_jumat = ' '
                    id_jumat   = 0
                if x == 6:
                    mapel_sabtu = '-'
                    guru_sabtu = ' '
                    id_sabtu    = 0
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
            "guru_senin"    : guru_senin,
            "guru_selasa"   : guru_selasa,
            "guru_rabu"     : guru_rabu,
            "guru_kamis"    : guru_kamis,
            "guru_jumat"    : guru_jumat,
            "guru_sabtu"    : guru_sabtu, 
            "kelas"         : kelas_id,
            "id_jadwalku"   : id_jadwal_ku,
            "id_senin"      : id_senin,
            "id_selasa"     : id_selasa,
            "id_rabu"       : id_rabu,
            "id_kamis"      : id_kamis,
            "id_jumat"      : id_jumat,
            "id_sabtu"      : id_sabtu,
           
            # "jadwal"         : jadwal,
      
            

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
    }
  
    template = 'penjadwalan/data_jadwal.html'
    return render (request, template, context)


def tambah_jadwal(request, kelas, hari, jamke):
    # url_jadwal = request.build_absolute_uri() 
    # get_info = Penjadwalan.objects.get(kelas=kelas, jamke = jamke)
    back_jadwal = Penjadwalan.objects.filter(kelas = kelas)

    url = str(request.get_full_path) 
    b = url.split('/')
    print ("print b", b)
    print("print b[5]", b[5])
    c = b[5]
    d = c.split("'")
    print("print d[0]", d[0])
  
    add_form = Ftambahjadwal(request.POST or None, initial={'kelas': b[3], 'hari' : b[4], 'jamke' : d[0]})
    cekguru = Guru.objects.filter(penjadwalan__hari=b[4], penjadwalan__jamke=d[0])
    cekdata = Penjadwalan.objects.filter(kelas=b[3], hari=b[4], jamke=d[0])
    print(cekguru)
    # # for i in cekguru:
    # #     jadwal = Penjadwalan.objects.filter(guru=i)
    # #     for x in jadwal:
    # #         print('kelas', x.kelas)
    # #         break
    # # print(cekguru)
    # # print("udah ada di ", kelasguru)

    if request.method == 'POST':
        if add_form.is_valid():
            form_save = add_form.save(commit=False)
            # if cekdata.exists():
            #     print("jadwal guru sudah terisi sebelumya")
            #     messages.error(request, 'jadwal guru sudah terisi sebelumya')
            #     return redirect('tambah_jadwal', kelas = kelas, hari=hari, jamke=jamke )
            
            if len(cekguru) >= 1:
                for i in cekguru:   #mendeteksi tabrakan
                    if i == form_save.guru:
                        jadwal = Penjadwalan.objects.filter(guru=i)
                        print("jadwal guru bertabrakan")
                        messages.error(request, 'Guru sudah mengajar di kelas ___ pada jam yang sama !')
                        return redirect('tambah_jadwal', kelas = kelas, hari=hari, jamke=jamke )
                        break
                    else:
                        print("jadwal tidak bertabrakan")
                        messages.success(request, 'Jadwal berhasil dimasukkan!')
                        add_form.save()
                        return redirect('jadwal', kelas_id = kelas)

            else:
                print("jadwal tidak bertabrakan")
                messages.success(request, 'Jadwal berhasil dimasukkan!')
                add_form.save()
                return redirect('jadwal', kelas_id = kelas)


        return redirect('jadwal', kelas_id = kelas)
    context = {
        
        'add_form'      : add_form,
        'back_jadwal'   : back_jadwal,
    }
    return render(request, 'penjadwalan/tambah_jadwal.html', context ) 

def tambah_jadwal2(request):
  
    add_form = Ftambahjadwal(request.POST or None)

    # # cekguru = Guru.objects.all()
    # # cekguru = Guru.objects.filter(penjadwalan__jamke= add_form['jamke'])
  
    if request.method == 'POST':
        if add_form.is_valid():
            value_form = add_form.save(commit=False)

            cekguru = Guru.objects.filter(penjadwalan__hari=value_form.hari, penjadwalan__jamke=value_form.jamke)
            print('value commit dapet', value_form.jamke)
            cekdata = Penjadwalan.objects.filter(kelas=value_form.kelas, hari=value_form.hari, jamke=value_form.jamke)

            if cekdata.exists():
                print("jadwal guru sudah terisi sebelumya")
                messages.error(request, 'jadwal guru sudah terisi sebelumya')
                return redirect('tambah_jadwal2')

            if len(cekguru) >= 1:
                for i in cekguru:   #mendeteksi tabrakan
                    if i == value_form.guru:
                        jadwal = Penjadwalan.objects.filter(guru=i)
                        print("jadwal guru bertabrakan")
                        messages.error(request, 'Guru sudah mengajar di kelas ___ pada jam yang sama !')
                        return redirect('tambah_jadwal2')
                        break
                    else:
                        print("jadwal tidak bertabrakan")
                        messages.success(request, 'Jadwal berhasil dimasukkan!')
                        add_form.save()
                        return redirect('jadwal', value_form.kelas.id)

            else:
                print("jadwal tidak bertabrakan")
                messages.success(request, 'Jadwal berhasil dimasukkan!')
                add_form.save()
                return redirect('jadwal', value_form.kelas.id)

        # return redirect('tambah_jadwal2')
    context = {
        'add_form': add_form,
    }
    return render(request, 'penjadwalan/tambah_jadwal2.html', context )  

def update_jadwal(request, kelas, hari, jamke):
    add_form = Ftambahjadwal(request.POST or None)
    jadwal_update = Penjadwalan.objects.get(kelas = kelas, hari = hari, jamke = jamke)
    jadwal = Penjadwalan.objects.filter(kelas = kelas, hari = hari, jamke = jamke)
    # jadwal2 = Penjadwalan.objects.get(kelas = kelas, hari = hari, jamke = jamke)
    back_jadwal = Penjadwalan.objects.filter(kelas = kelas)

    data = {
        'kode_jampel'   : jadwal_update.kode_jadwal,
        'kelas'         : jadwal_update.kelas,
        'hari'          : jadwal_update.hari,
        'jamke'         : jadwal_update.jamke,
        'guru'          : jadwal_update.guru,
        'mapel'         : jadwal_update.mapel,
        
    }
    add_form = Ftambahjadwal(request.POST or None, initial=data, instance=jadwal_update)
    cekdata = Guru.objects.filter(penjadwalan__kelas_id=data['kelas'].id, penjadwalan__hari=data['hari'], penjadwalan__jamke=data['jamke'])
    cekguru = Guru.objects.filter(penjadwalan__hari=data['hari'], penjadwalan__jamke=data['jamke'])
    # cekdata = Penjadwalan.objects.filter(kelas=value_form.kelas, hari=value_form.hari, jamke=value_form.jamke)

    if request.method == 'POST':
        form_save = add_form.save(commit=False)

        # if cekdata.exists():
        #     print("jadwal guru sudah terisi sebelumya")
        #     messages.error(request, 'jadwal guru sudah terisi sebelumya')
        #     return redirect('tambah_jadwal', kelas = kelas, hari=hari, jamke=jamke )
        
        if len(cekguru) > 1:
            for i in cekguru:   #mendeteksi tabrakan
                if i == form_save.guru:
                    jadwal = Penjadwalan.objects.filter(guru=i)
                    print("jadwal guru bertabrakan")
                    messages.error(request, 'Guru sudah mengajar di kelas ___ pada jam yang sama !')
                    return redirect('update_jadwal', kelas = kelas, hari=hari, jamke=jamke )
                    break
                else:
                    print("jadwal tidak bertabrakan")
                    messages.success(request, 'Jadwal berhasil dimasukkan!')
                    add_form.save()
                    return redirect('jadwal', kelas_id = kelas)

        else:
            print("jadwal tidak bertabrakan")
            messages.success(request, 'Jadwal berhasil dimasukkan!')
            add_form.save()
            return redirect('jadwal', kelas_id = kelas)


        return redirect('jadwal', kelas_id = kelas)
 
    context = {
        'add_form'      : add_form,
        'back_jadwal'   : back_jadwal,
        'jadwal_hapus'  : jadwal,

    }
    return render(request, 'penjadwalan/update_jadwal.html', context )

def delete_jadwal(request, id_delete):
    Penjadwalan.objects.filter(id=id_delete).delete()
  
    print("terhapus!!")
    messages.warning(request, 'Jadwal berhasil dihapus!')
    return redirect('data_jadwal')








# def index_coba(request):
#     context = {
#         'page title' : 'HOME',
#     }
#     # print(request.user)
#     username_sel = 'selpong'
#     password_sel = 'selvia123'
#     user = authenticate(request, username = username_sel, password = password_sel)
#     print(user)
#     login(request, user)
#     return render(request, 'index_coba.html', context)

# selected_kelas = Kelas.objects.get(pk = 1)
# kelas_id = 1
# mkelas = Kelas.objects.filter(id = kelas_id)
# for i in mkelas:
#     print (i.id)

