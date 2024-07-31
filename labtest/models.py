from django.db import models

# Create your models here.
class Procedure(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
                
    def __str__(self):
        return self.name

class LabTest(models.Model):
    patient_name = models.CharField(max_length=100)
    test_name = models.CharField(max_length=100)
    test_date = models.DateField()
    result = models.TextField()
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
                                    
    def __str__(self):
        return f"{self.test_name} for {self.patient_name} on {self.test_date}"
