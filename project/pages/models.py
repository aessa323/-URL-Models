from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=150)
    university_id = models.CharField(max_length=20, unique=True)
    age = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='students/')

    def __str__(self):
        return self.full_name