from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
"""
We will be extending our custom users, the built in user models are often not sufficient for large scale projects.
"""

#I am going override the admin user so that we don't have to use the email
class MyAccountManager(BaseUserManager):
    #create base user

    def create_user(self,first_name,last_name,username,email,password=None):
        """
        This method can then be used in a form to create a user.
        """
        #this is just basic validation
        if not email:
            raise ValueError("user must have an email address")

        if not username:
            raise ValueError("user must have an username")

        user = self.model(
            email = self.normalize_email(email), #this normalize email method normalize all the caps in a supposed email
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
        
    #create a super user account based on basic user
    def create_superuser(self,email,first_name,last_name,username,password):
        user = self.create_user(
            email = self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        
        #let's give our superuser permissions
        user.is_admin = True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user



#create an account for the website
class Author(AbstractBaseUser): 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=200,unique=True)
    phone_number = models.CharField(max_length=50)

    #required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email' # this allow us to login with our email address
    REQUIRED_FIELDS = ['username','first_name','last_name']

    objects = MyAccountManager() #this gives MyAccountManager rights to control all the users

    def __str__(self):
        return self.email

    #I override the permission method, if a user is an admin he/she can make changes
    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,add_label):
        return True

    






