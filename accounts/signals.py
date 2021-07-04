from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.contrib.auth.models import User
from accounts.models import Profile
from django.conf import settings
User = settings.AUTH_USER_MODEL

# writing this methods in signal.py will trigger this method everytime a new user is created or  updated
# and it will save all the instances in Profile model
# so now each User in django model will have profile automatically
@receiver(post_save, sender = User)    
def create_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
        print('Profile Created')
          
# in  place of the above decorator we can use 'post_save.connect'method to connect the signals
# post_save.connect(create_profile, sender = User)


@receiver(post_save, sender=User)
def update_profile(sender,instance,created, **kwargs):
    if created == False:
        instance.profile.save()
        print("Profile updated!!")
        


# post_save.connect(update_profile, sender = User)
