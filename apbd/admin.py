from django.contrib import admin
from .models import Anggaran, News

@admin.register(Anggaran)
class AnggaranAdmin(admin.ModelAdmin):
    list_display = ('tahun', 'sektor', 'alokasi', 'deskripsi')
    list_filter = ('tahun', 'sektor')
    search_fields = ('sektor', 'deskripsi')
    list_editable = ('alokasi',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')  # created_at sudah dihapus sebelumnya
    list_filter = ('date',)
    search_fields = ('title', 'content')
    date_hierarchy = 'date'
    fields = ('title', 'content', 'date', 'link', 'image')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['image'].required = True  # Mewajibkan upload gambar
        return form