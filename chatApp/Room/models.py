from venv import create
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=250)
    slug=models.SlugField()
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Message(models.Model):
    content=models.CharField(max_length=250)
    
 
    def __str__(self):
        return self.content[0:100]   
class HistoryChatApp(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    message=models.ForeignKey(Message,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    

from django.db.models.signals import pre_save
from django.dispatch import receiver
from App.consumer import chatConsumer
@receiver(pre_save,sender=Message)
def hello(sender,**kwargs):
    print("hello")


    
    