from django import forms

from .models import Sales, Fertilizers, Employee, Seedlings


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['Employee_ID', 'First_Name', 'Last_Name', 'DOB', 'ID_Number', 'Mobile_Number', 'E_mail',
                  'Employment_date', 'Termination_date', 'Salary']


class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['Sales_ID', 'Product_Sold', 'Quantity_Sold', 'Price', 'Date']


class SeedlingsForm(forms.ModelForm):
    class Meta:
        model = Seedlings
        fields = ['Seedling_ID', 'Crop_type', 'Quantity', 'Purchase_Date', 'Expected_Planting_Date', 'Price']


class FertilizersForm(forms.ModelForm):
    class Meta:
        model = Fertilizers
        fields = ['Fert_Chem_ID', 'Fert_Chem_Name', 'Company', 'Quantity', 'Dosage', 'Date_of_Purchase',
                  'Expiry_Date', 'Price']


class UpdateMobileNumber(forms.Form):
    Employee_ID = forms.CharField(max_length=12, required=True)
    Mobile_Number = forms.IntegerField(required=True)

    class Meta:
        fields = ('Employee_ID', 'Mobile_number')


class UpdateEmail(forms.Form):
    Employee_ID = forms.CharField(max_length=12, required=True)
    E_mail = forms.EmailField(required=True)


class UpdateTerminationDate(forms.Form):
    Employee_ID = forms.CharField(max_length=12, required=True)
    Termination_Date = forms.DateField(required=True)


class UpdateSalary(forms.Form):
    Employee_ID = forms.CharField(max_length=12, required=True)
    Salary = forms.IntegerField(required=True)
