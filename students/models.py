from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)

    age = models.PositiveSmallIntegerField()

    english_marks = models.PositiveSmallIntegerField()

    maths_marks = models.PositiveSmallIntegerField()

@property
def total_marks(self):
    return self.english_marks + self.maths_marks

@property
def result(self):
    if self.english_marks >= 35 and self.maths_marks >= 35:
        return "Pass"
    return "Fail"

def __str__(self):
    return self.name