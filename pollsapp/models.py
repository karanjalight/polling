from django.db import models
from django.db.models.signals import post_save
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings



# Create your models here.
# class Account(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     status = status = models.BooleanField(default=False)

#     def __str__(self):
#         return '{}, {}'.format(self.user.username, self.status)

class Question(models.Model):
    question = models.CharField(max_length=300)

    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    option = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)
    userid = models.CharField(max_length=20, unique=True)
    #idnumber = models.CharField( max_length=100, unique= False)
    
    

    def __str__(self):
        return self.option


