from django.db import models

class Member(models.Model):
    mid=models.IntegerField(default=101)
    name=models.CharField(max_length=264)
    fname=models.CharField(max_length=264)
    gender=models.CharField(max_length=264)
    address=models.CharField(max_length=264)
    pincode=models.CharField(max_length=264)
    postoffice=models.CharField(max_length=264)
    district=models.CharField(max_length=264)
    state=models.CharField(max_length=264)
    mno=models.CharField(max_length=264,unique=True)
    adhar=models.CharField(max_length=264,unique=True)
    email=models.CharField(max_length=264)

    def __str__(self):
        return self.name
    





    

