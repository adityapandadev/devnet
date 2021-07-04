from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE



# Create your models here.

# Model for handling Feed Post data

class Post(models.Model):
    caption = models.CharField(max_length=60)
    image = models.ImageField(upload_to ="media/", name = "image", blank = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,null = True,default =1,on_delete = CASCADE)
 
    def __str__(self):
        return(self.caption)
