from django.db import models

# Create your models here.
class Contact(models.Model):
	email = models.EmailField(max_length=64,unique=True)
	subject = models.CharField(max_length=64)
	message = models.TextField()