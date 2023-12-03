from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    is_special_user = models.BooleanField(default=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],blank=True, null=True)
    special_users = models.ManyToManyField(User, related_name='special_users', blank=True)
    selected_users = models.ManyToManyField(User, related_name='selected_users', blank=True)  # 새로 추가한 부분

    def __str__(self):
        return self.user.username