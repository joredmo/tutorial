from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True) # auto_now_add = True means that the field will be updated every time the object is saved
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'notes') # on_delete =
    
    def __str__(self):
        return self.title

# Create your models here.
