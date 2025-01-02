from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField()
    technologies_used = models.CharField(max_length=300, default="Not specified")
    image = models.ImageField(upload_to='projects/') 
    link = models.URLField(blank=True, null=True)  
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    def __str__(self):
        return self.title


class Contact(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    number=models.IntegerField()
    message=models.TextField(max_length=300)
    submitted=models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.Name
    

class certificates(models.Model):
    image=models.ImageField(upload_to='projects/',null=True,blank=True) 
    name=models.CharField(max_length=300)
