from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='news_images/')

    def __str__(self):
        return self.title

class Anggaran(models.Model):
    sektor = models.CharField(max_length=100)
    tahun = models.IntegerField()
    alokasi = models.DecimalField(max_digits=15, decimal_places=2)
    deskripsi = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.sektor} ({self.tahun})"