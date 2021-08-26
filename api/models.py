from django.db import models
import string
import random
# Create your models here.
#the rule is fat model and thin views

def genrate_unique_code():
    length=6
    while True:
        code=''.join(random.choices(string.ascii_uppercase,k=length))
        if Room.objects.filter(code=code).count()==0:
            break
    return code

class Room(models.Model):   #model to group similar users
    code=(models.CharField(default=genrate_unique_code, max_length=8,unique=True))
    host=models.CharField(max_length=50,unique=True)
    guests_can_pause=models.BooleanField(null=False,default=False,)
    votes_to_skip=models.IntegerField(null=False,default=1)
    created_at=models.DateTimeField(auto_now_add=True)
