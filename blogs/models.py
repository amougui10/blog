from django.db import models
from django.conf import settings

from PIL import Image
# Create your models here.
from django.conf import settings

class Photo(models.Model):
    
    image = models.ImageField()
    caption = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created  = models.DateTimeField(auto_now_add=True)
    IMAGE_MAX_SIZE = (800, 800)
    
    def risize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.risize_image()
        
        
    
    
class Blog (models.Model):
    
        
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    contributors = models.ManyToManyField(settings.AUTH_USER_MODEL, through='BlogContributor', related_name='contributions')
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=5000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
    words_count = models.IntegerField(null = True)
    
    
    def _get_words_count(self):
        return len(self.content.split(' '))

    def save(self, *args, **kwargs):
        self.word_count = self._get_words_count()
        super().save(*args, **kwargs)


class BlogContributor(models.Model):
    
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    contribution = models.CharField(max_length=255, blank=True)
    
    
    class Meta:
        unique_together = ('contributor', 'blog')
    