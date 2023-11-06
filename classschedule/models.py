from django.db import models

# Create your models here.
class PersonalData(models.Model):
   name=models.CharField(max_length=100)
   age=models.IntegerField()
   classroom_number=models.IntegerField(default=2)

   def __str__(self):
      return f"{self.name}:classroom{self.classroom_number}on age{self.age}"




class ClassSchedule(models.Model):
   #state column ids to be used for reference
   topic=models.CharField(max_length=200)
   date=models.DateTimeField()
   start_time=models.TimeField(default=2)
   classroom=models.ForeignKey(PersonalData,on_delete=models.CASCADE,default=1)

