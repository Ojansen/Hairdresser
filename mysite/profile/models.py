from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group


class MyAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have an first_name")

        user = self.model(email=self.normalize_email(email),
                           first_name=first_name,
                           last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(email=self.normalize_email(email),
                                first_name=first_name,
                                last_name=last_name,
                                password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Profile(AbstractBaseUser):
    username = None
    email = models.EmailField(max_length=60, unique=True, verbose_name='email')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile_nr = models.IntegerField(null=True)
    address = models.CharField(max_length=60, null=True)
    loyalty_points = models.IntegerField(null=True, default=0)
    groups = models.ManyToManyField(Group)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.first_name + " " + self.last_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_absolute_url(self):
        return reverse('profile:profile-detail')

    class Meta:
        pass
