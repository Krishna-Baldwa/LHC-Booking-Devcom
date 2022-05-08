from django.db import models

# Create your models here.
class halls(models.Model):
    Lecture_Hall_Name=models.CharField(max_length=25)
    Occupancy_status=models.CharField(max_length=20)
    hall_id=models.IntegerField()

    def __str__(self):
        return self.Lecture_Hall_Name
