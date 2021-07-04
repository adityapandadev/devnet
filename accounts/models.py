from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.db.models.deletion import CASCADE
from post.models import Post
from django.conf import settings
User = settings.AUTH_USER_MODEL

# We need to make user login through mobile number , so i used a custom user model which extends Abstract User Model 

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, mobile, password=None, **extra_fields):
        """Create and save a User with the given mobile and password."""
        if not mobile:
            raise ValueError('The given mobile must be set')
        # mobile = self.normalize_mobile(mobile)
        user = self.model(mobile=mobile,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, mobile, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(mobile, password, **extra_fields)

    def create_superuser(self, mobile, password=None, **extra_fields):
        """Create and save a SuperUser with the given mobile and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(mobile, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    mobile = models.CharField(_('Mobile Number'),validators=[RegexValidator("^0?[5-9]{1}\d{9}$")],max_length=20,unique=True)
    friends = models.ManyToManyField("CustomUser",blank=True)


    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


# Model to store profile information
class Profile(models.Model):
    user = models.OneToOneField(to = User,on_delete = CASCADE)
    post = models.ForeignKey(Post,on_delete = CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.user.first_name


class Friend_Request(models.Model):
    from_user = models.ForeignKey(CustomUser, related_name='from_user',on_delete=models.CASCADE)
    to_user = models.ForeignKey(CustomUser, related_name='to_user',on_delete=CASCADE)    
