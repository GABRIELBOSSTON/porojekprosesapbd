from django.shortcuts import render
from .models import News, Anggaran

def index(request):
    news_list = News.objects.all().order_by('-date')[:8]  # Ubah dari [:4] menjadi [:8]
    anggaran_list = Anggaran.objects.all().order_by('-tahun')[:3]
    return render(request, 'apbd/index.html', {'news_list': news_list, 'anggaran_list': anggaran_list})

def informasi(request):
    return render(request, 'apbd/informasi.html')

def unduh(request):
    return render(request, 'apbd/unduh.html')

def akun(request):
    if request.method == 'POST':
        # Placeholder untuk logika login
        pass
    return render(request, 'apbd/akun.html')

def faq(request):
    return render(request, 'apbd/faq.html')

