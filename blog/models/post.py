from django.db import models
from autoslug import AutoSlugField
from blog.models import CategoryModel
from django.contrib.auth.models import User

class PostModel(models.Model):
    image = models.ImageField(upload_to='post_images')
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True) # Yazılar tablosu bir kayıt oluşturulduğu zaman oluşturulma tarihi otomatik olarak belirlenecek. Timezone ile yapılabilir.
    edited_date = models.DateTimeField(auto_now=True) # İçerik her değiştirildiğinde düzenlenme tarihi otomatik yenilenecek.
    slug = AutoSlugField(populate_from="title",unique=True)
    categories = models.ManyToManyField(CategoryModel,related_name='post') # 1 yazı, 1 den fazla kategoriye atılabilir.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        db_table = 'post'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.title