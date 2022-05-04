from django.db import models

# Create your models here.
class CSVfiles(models.Model):

    file=models.FileField(
        upload_to='files/',
    )



class Employees(models.Model):
    EmpID=models.IntegerField()
    ProjectID=models.IntegerField()
    DateFrom=models.DateField()
    DateTo=models.DateField(
        null=True
    )


class Result(models.Model):
    duration=models.IntegerField()
    project_id=models.IntegerField()
    first_emp_id=models.IntegerField()
    second_emp_id=models.IntegerField()


