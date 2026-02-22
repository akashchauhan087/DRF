from django.db import models

GENDER_LIST = [('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('ANY', 'ANY')]
BLOOD_GROUP_LIST = (('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-'))

class Employee(models.Model):
    name= models.CharField(max_length=50, null=True, blank=True)
    age= models.PositiveIntegerField(default=18, null=True, blank=True)
    designation= models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(choices=GENDER_LIST, default='MALE', null=True, blank=True)
    blood_group = models.CharField(choices=BLOOD_GROUP_LIST, null=True, blank=True)
    father_name= models.CharField(max_length=50, null=True, blank=True)
    mother_name= models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
