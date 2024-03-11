from django.db import models

# Create your models here.

class student(models.Model):
    #  id = models.IntegerField(max_length=10)
     fname = models.CharField(max_length=50)
     mail = models.EmailField(unique=True)
     dob = models.DateField(max_length=10)
     phone = models.CharField(max_length=50)
     p_phone = models.CharField(max_length=50)
     address = models.CharField(max_length=50)

     
     def __str__(self):
         return f"{self.fname}{self.id}{self.email}{self.dob}{self.phone}{self.p_phone}{self.address}"
     
class Leture(models.Model):
     tname = models.CharField(max_length=50)
     up = models.DateField(max_length=10)
    #  upfile= models.CharField(max_length=50)

     def __str__(self):
         return f"{self.tname}{self.id}{self.up}"
     
class CourseJ(models.Model):
     tname = models.CharField(max_length=50)
     up = models.DateField(max_length=10)
    #  upfile= models.CharField(max_length=50)

     def __str__(self):
         return f"{self.tname}{self.id}{self.up}"

class CourseH(models.Model):
     tname = models.CharField(max_length=50)
     up = models.DateField(max_length=10)
    #  upfile= models.CharField(max_length=50)

     def __str__(self):
         return f"{self.tname}{self.id}{self.up}"


class Assignment(models.Model):
     tname = models.CharField(max_length=50)
     up = models.DateField(max_length=10)
     titles = models.CharField(max_length=50)
     des = models.CharField(max_length=50)
     asgn = models.CharField(max_length=50)
    #  upfile= models.CharField(max_length=50)

     def __str__(self):
         return f"{self.tname}{self.id}{self.up}{self.titles}{self.asgn}{self.des}"
     
class Notes(models.Model):
     tname = models.CharField(max_length=50)
     up = models.DateField(max_length=10)
    #  upfile= models.CharField(max_length=50)

     def __str__(self):
         return f"{self.tname}{self.id}{self.up}"

class Tests(models.Model):
     tname = models.CharField(max_length=50)
     up = models.DateField(max_length=10)
    #  upfile= models.CharField(max_length=50)

     def __str__(self):
         return f"{self.tname}{self.id}{self.up}"
