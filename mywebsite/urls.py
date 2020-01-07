from django.contrib import admin
from penjadwalan import views
from django.urls import path,include


urlpatterns = [
    # admin
    path('login_success', views.login_success, name='login_success'),
    path('index', views.index_coba, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('login/', views.page_login, name='page_login'),
    path('data/', include('penjadwalan.urls')),
    path('adm', views.index, name = 'index'),
    path('', views.index, name = 'index'),

    path('data_tables', views.data_tables, name='data_tables'),
    path('base', views.base, name='base'),
    path('user/',include('userweb.urls', namespace='generalweb')),
    # path('',include('userweb.urls', namespace='generalweb')),

    path('signup', views.signup, name='signup'),

]
 


 # path('delete_guru/(?P<id_delete>[0-9])', views.delete_guru, name='delete_guru' ),
 # path('tambah_guru', views.tambah_guru, name='tambah_guru'), 
 # path('data_guru', views.data_guru, name='data_guru'),