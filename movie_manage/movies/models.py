from django.db import models

class censorinfo(models.Model):
    rating=models.CharField(max_length=100,null=True)
    certifiedby=models.CharField(max_length=200,null=True)

class director(models.Model):
    director_name = models.CharField(max_length=100)

    def __str__(self):
        return self.director_name

class movieinfo(models.Model):
    title = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    actress = models.CharField(max_length=100)
    poster=models.ImageField(upload_to='images/',null=True)
    year = models.IntegerField(null=True)
    censordetails=models.OneToOneField(censorinfo,on_delete=models.SET_NULL,related_name='movie',null=True)
    directedby=models.ForeignKey(director,on_delete=models.CASCADE,null=True,related_name='director')

    def __str__(self):
        return self.title
    
