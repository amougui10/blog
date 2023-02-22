from django.db import models
from django.contrib.auth.models import AbstractUser, Group
# Create your models here.


class User(AbstractUser):
  
    
    CREATOR = "CREATOR"
    SUBSCRIBER = "SUBSCRIBER"
    
    
    ROLE_CHOICE = (
		(CREATOR,'createur'),
		(SUBSCRIBER,'abonné'),
	)
    
    profile_photo = models.ImageField(verbose_name='photo de profile')
    role = models.CharField(max_length=10, choices= ROLE_CHOICE, verbose_name='Role')
    follows = models.ManyToManyField('self',
                                     limit_choices_to={'role':CREATOR} , symmetrical=False, verbose_name='suit')
    def save(self, *args, **kwargs):
      super().save(*args, **kwargs)
      
      if self.role == self.CREATOR:
        group = Group.objects.get(name = 'creators')
        group.user_set.add(self)
      elif self.role ==self.SUBSCRIBER:
        group = Group.objects.get(name ='subscribers')
        group.user_set.add(self)
    

    
