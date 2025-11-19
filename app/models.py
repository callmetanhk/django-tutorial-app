from django.db import models
from django.contrib.auth.models import User

def upload_avatar(instance, filename):
    return f"avatars/{instance.user.id}/{filename}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to=upload_avatar, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=(('male', 'Male'), ('female', 'Female'), ('other', 'Other')),
        default='other'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "profile"

    def __str__(self):
        return self.full_name
