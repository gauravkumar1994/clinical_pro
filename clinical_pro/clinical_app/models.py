from django.db import models

# Create your models here.
class Patient(models.Model):
    firstname=models.CharField(max_length=120)
    lastname=models.CharField(max_length=140)
    age=models.IntegerField()

class ClinicalData(models.Model):
    COMPONENT_NAMES = (
    ("hw", "height/weight"),
    ("bp", "blood presure"),
    ("heartrate", "Heart Rate")
)
    componentname=models.CharField(max_length=120,choices =COMPONENT_NAMES,default = 'select any one')
    componentvalue=models.CharField(max_length=140)
    measureDATETIME=models.DateTimeField(auto_now_add=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)