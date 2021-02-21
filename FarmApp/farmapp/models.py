from django.db import models


class Employee(models.Model):
    Employee_ID = models.CharField(max_length=12, primary_key=True)
    First_Name = models.CharField(max_length=15)
    Last_Name = models.CharField(max_length=15)
    ID_Number = models.IntegerField()
    DOB = models.DateField()
    Mobile_Number = models.IntegerField()
    E_mail = models.EmailField()
    Employment_date = models.DateField()
    Termination_date = models.DateField(blank=True, null=True)
    Salary = models.IntegerField()


class Fertilizers(models.Model):
    Fert_Chem_ID = models.CharField(max_length=12, primary_key=True)
    Fert_Chem_Name = models.CharField(max_length=75)
    Company = models.CharField(max_length=25)
    Expiry_Date = models.DateField()
    Quantity = models.IntegerField()
    Date_of_Purchase = models.DateField()
    Dosage = models.CharField(max_length=25)
    Price = models.IntegerField()


class Seedlings(models.Model):
    Seedling_ID = models.CharField(max_length=15, primary_key=True)
    Expected_Planting_Date = models.DateField()
    Purchase_Date = models.DateField()
    Quantity = models.IntegerField()
    Crop_type = models.CharField(max_length=30)
    Price = models.IntegerField()


class Sales(models.Model):
    Sales_ID = models.CharField(primary_key=True, max_length=15)
    Product_Sold = models.CharField(max_length=50)
    Date = models.DateField()
    Quantity_Sold = models.IntegerField()
    Price = models.IntegerField()
    Sales_Made = models.IntegerField()
