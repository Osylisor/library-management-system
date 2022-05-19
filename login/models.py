from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser



class MyUserManager(BaseUserManager):

    def create_user(self, email, name,  password = None):


        if not email:
            ValueError('Users must have an email address')

        new_user = self.model(email = self.normalize_email(email),
                                name = name)
        new_user.set_password(password)
        new_user.save(using = self._db)
        return new_user

    def create_admin_user(self, email, name, password = None):

        new_user = self.create_user(email, name, password)
        new_user.is_admin = True
        new_user.save(using = self._db)
        return new_user


class User(AbstractBaseUser):

    email = models.EmailField(max_length=120,  unique=True)
    name = models.CharField(max_length=200, blank=True)
    student_number = models.CharField(max_length=200)
    is_admin = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to = 'images', blank = True, null= True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = MyUserManager()



