from django.db import models

# Create your models he
class User(models.Model):
    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    profile_pic = models.URLField()
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
