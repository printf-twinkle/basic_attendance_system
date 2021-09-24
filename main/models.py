from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.deletion import CASCADE 


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
			email=self.normalize_email(email),
			username=username,
		)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

 
class User(AbstractBaseUser):
    name = models.CharField(max_length=255, null=True,blank=True)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    roll_number = models.IntegerField(null=True, blank=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_present = models.BooleanField(default=False)
    is_request = models.BooleanField(default=False)
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)

    objects = MyAccountManager()
    USERNAME_FIELD = 'email'
    search_fields = ("name", "email")
    REQUIRED_FIELDS = ['username']


    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.name or ''

 