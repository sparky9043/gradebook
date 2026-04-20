from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'people'
    
    def __str__(self):
        return self.name

class Student(Person):
    student_id = models.CharField(max_length=50)
    grade = models.IntegerField(choices=[(9, 9), (10, 10), (11, 11), (12, 12)])
    
    def __str__(self):
        return f"Grade: {self.grade} {self.name}"