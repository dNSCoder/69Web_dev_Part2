from django.db import models
from django.contrib.auth.models import User

def user_avatar_path(instance, filename):
    ext = filename.split('.')[-1] # ดึงเอานามสกุล ของไฟล์
    return f"avatars/user_{instance.user.id}/avatar.{ext}" #คืน path สำหรับการสร้างรูปภาพและตั้งชื่อไฟล์ใหม่

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=user_avatar_path, blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username