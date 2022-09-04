from core.views import Deslogeo,Logeando,SignIn,home,departamentos,hoteles,resorts,villas,Registros,admin,SignUp
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='index'),
    path('departamentos/', departamentos, name='departamentos'),
    path('hoteles/', hoteles, name='hoteles'),
    path('resorts/', resorts, name='resorts'),
    path('villas/', villas, name='villas'),
    path('admin2/', admin, name='admin'),
    # Sign In
    path('signin/', SignIn, name='SignIn'),
    path('signup/', SignUp, name='SignUp'),
    path('registro/', Registros, name='Registros'),
    path('signin/logeando/', Logeando, name='Logeando'),
    path('signin/deslogeando/', Deslogeo, name='Deslogeo'),

]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)