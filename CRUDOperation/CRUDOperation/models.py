from django.db import models  
class EmpModel(models.Model):    
    ename = models.CharField(max_length=100)   
    contact = models.IntegerField() 
    salary = models.IntegerField() 
    gender = models.CharField(max_length=100)  
    class Meta:  
        db_table = "employee"  