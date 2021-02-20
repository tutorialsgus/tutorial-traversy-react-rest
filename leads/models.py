from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.DateField(auto_now_add=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # tipo um valor de default