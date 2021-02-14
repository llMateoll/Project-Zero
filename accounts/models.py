from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    phone = models.TextField(max_length=20, null=True, blank=True)
    money = models.DecimalField(max_digits=30, decimal_places=2, default='0.00')
    referenceID = models.TextField(max_length=20, null=False, blank=False)

    class Meta:
        ordering = ['id']

    # def __str__(self):
    #     return self.user

    # pk = models.Field(primary_key = True)