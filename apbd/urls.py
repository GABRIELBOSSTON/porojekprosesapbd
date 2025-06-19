from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('informasi/', views.informasi, name='informasi'),
    path('unduh/', views.unduh, name='unduh'),
    path('akun/', views.akun, name='akun'),
    path('faq/', views.faq, name='faq'),
]

def akun(request):
    if request.method == 'POST':
        # Placeholder untuk logika login
        pass
    return render(request, 'apbd/akun.html')