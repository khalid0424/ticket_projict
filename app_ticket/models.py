from django.db import models




class Movie(models.Model):
    tittle = models.CharField(max_length= 100)
    genr = models.CharField(max_length=56)
    publicdate = models.DateField()
    teatr =models.CharField()
    description = models.CharField(max_length=500)
    image_poster= models.ImageField(upload_to='static/images', blank=True)
    
    def __str__(self):
      return self.tittle

class Teatr(models.Model):
   name = models.CharField(max_length=55)
   teatraddres = models.CharField(max_length=77)


   def __str__(self):
      return  self.name
   
class Show(models.Model):
   movie = models.CharField(max_length=50)
   teatr = models.CharField(max_length=78)
   date = models.DateField(db_default=0)
   time = models.DateTimeField(auto_now=None)
   trilevideo = models.FileField(upload_to='static/video', blank=True)


   def __str__(self):
      return self.movie
   

class Ticketorder(models.Model):
   timeshow =models.DateField(auto_now_add= None)
   name_kilent = models.CharField(max_length=88)
   number_kilent = models.CharField(max_length= 199)
   ticket_summa = models.CharField(max_length=1000000)
   data_payment = models.DateTimeField(null=0)


   def __str__(self):
      return self.timeshow