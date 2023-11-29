from django.db import models

# Create your models here.

class UploadImage(models.Model):
    image = models.ImageField(upload_to='img/')
    title = models.CharField(max_length=200, verbose_name="タイトル")
    detail = models.TextField(verbose_name="詳細")
    point = models.TextField(verbose_name="頑張ったところ")
    dissapoint = models.TextField(verbose_name="直したいところ")
    like = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

