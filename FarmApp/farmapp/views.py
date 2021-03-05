import calendar
from datetime import datetime

from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.db.models import Sum

from farmapp.forms import SalesForm, SeedlingsForm, FertilizersForm, EmployeesForm,\
    UpdateEmail, UpdateTerminationDate, UpdateSalary, UpdateMobileNumber
from farmapp.models import Sales, Seedlings, Fertilizers, Employee


@csrf_protect
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            message = 'Incorrect username or password'
            form = AuthenticationForm()
            return render(request, 'login.html', {'login': form, 'message': message})

    form = AuthenticationForm()
    return render(request, 'login.html', {'login': form})


def log_out(request):
    logout(request)
    return redirect('/login')


def yearly(year):
    i = 0
    main_array = []
    while i < 5:
        yearly_sales = Sales.objects.filter(Date__year=year).aggregate(Sum('Sales_Made'))
        yearly_sales = list(yearly_sales.values())[0]

        if yearly_sales is None:
            yearly_sales = 0

        array = [year, yearly_sales]
        main_array.append(array)
        i = i + 1
        year = year - 1
    return main_array


def monthly(month, year):
    i = 0
    main_array = []
    while i < 12:
        monthly_sales = Sales.objects.filter(Date__year=year).filter(Date__month=month).aggregate(Sum('Sales_Made'))
        monthly_sales = list(monthly_sales.values())[0]

        salaries = Employee.objects.filter(Termination_date__isnull=True).aggregate(Sum('Salary'))
        fertilizers_monthly_cost = Fertilizers.objects.filter(Date_of_Purchase__month=month).aggregate(Sum('Price'))
        seedling_crop_cost = Seedlings.objects.filter(Purchase_Date__month=datetime.today().month).aggregate(Sum('Price'))

        salaries = list(salaries.values())[0]
        fertilizers_monthly_cost = list(fertilizers_monthly_cost.values())[0]
        seedling_crop_cost = list(seedling_crop_cost.values())[0]

        if salaries is None or fertilizers_monthly_cost is None or seedling_crop_cost is None:
            if salaries is None:
                salaries = 0
            if seedling_crop_cost is None:
                seedling_crop_cost = 0
            if fertilizers_monthly_cost is None:
                fertilizers_monthly_cost = 0

        monthly_expenditure = salaries + seedling_crop_cost + fertilizers_monthly_cost

        if monthly_sales is None:
            monthly_sales = 0

        month_n = calendar.month_abbr[month]
        profit = monthly_sales-monthly_expenditure
        array = [month_n, monthly_sales, monthly_expenditure, profit]
        main_array.append(array)

        i = i + 1
        if month > 1:
            month = month - 1
        else:
            year = year-1
            month = 12
    return main_array


@login_required(login_url='/login')
def home(request):
    user = request.user
    year = datetime.today().year
    month = datetime.today().month

    yearly_sales = dict(yearly(year))

    monthly_sales = monthly(month, year)
    employee = Employee.objects.filter(Termination_date__isnull=True)

    return render(request, 'home.html', {'user': user, 'employees': employee,
                                         'monthly_sales': monthly_sales, 'yearly_sales': yearly_sales, 'year': year})


def employees(request):
    form = EmployeesForm()
    form1 = UpdateMobileNumber()
    form2 = UpdateSalary()
    form3 = UpdateTerminationDate()
    form4 = UpdateEmail()
    employee = Employee.objects.all()
    try:
        if request.method == "POST":
            model = Employee()
            model.First_Name = request.POST.get('First_Name')
            model.Last_Name = request.POST.get('Last_Name')
            model.Mobile_Number = request.POST.get('Mobile_Number')
            model.E_mail = request.POST.get('E_mail')
            model.Employee_ID = request.POST.get('Employee_ID')
            model.Employment_date = request.POST.get('Employment_date')
            model.ID_Number = request.POST.get('ID_Number')
            model.DOB = request.POST.get('DOB')
            model.Salary = request.POST.get('Salary')

            if request.POST.get('Termination_date') == '':
                model.save()
            else:
                model.Termination_date = request.POST.get('Termination_date')

            message = "Employee saved"
            return render(request, 'employees.html', {'form': form, 'message': message, 'employee': employee})
    except:
        message = "Date format or date is incorrect!!"
        return render(request, 'employees.html', {'form': form, 'message': message, 'employee': employee})
    return render(request, 'employees.html', {'form': form, 'form1': form1, 'form2': form2, 'form3': form3,
                                              'form4': form4, 'employee': employee})


def chemicals_fertilizers(request):
    form = FertilizersForm()
    fertilizer = Fertilizers.objects.all()

    try:
        if request.method == 'POST':
            model = Fertilizers()
            model.Quantity = request.POST.get('Quantity')
            model.Expiry_Date = request.POST.get('Expiry_Date')
            model.Dosage = request.POST.get('Dosage')
            model.Company = request.POST.get('Company')
            model.Date_of_Purchase = request.POST.get('Date_of_Purchase')
            model.Fert_Chem_Name = request.POST.get('Fert_Chem_Name')
            model.Fert_Chem_ID = request.POST.get('Fert_Chem_ID')
            model.Price = request.POST.get('Price')
            model.save()
            message = "Chemical or fertilizer recorded"
            return render(request, 'chemfert.html', {'form': form, 'message': message, 'fertilizer': fertilizer})
    except:
        message = "Date or format is incorrect!!"
        return render(request, 'chemfert.html', {'form': form, 'message': message, 'fertilizer': fertilizer})
    return render(request, 'chemfert.html', {'form': form, 'fertilizer': fertilizer})


def seedling_crop(request):
    form = SeedlingsForm()
    seedlings = Seedlings.objects.all()

    try:
        if request.method == 'POST':
            model = Seedlings()
            model.Expected_Planting_Date = request.POST.get('Expected_Planting_Date')
            model.Quantity = request.POST.get('Quantity')
            model.Seedling_ID = request.POST.get('Seedling_ID')
            model.Crop_type = request.POST.get('Crop_type')
            model.Purchase_Date = request.POST.get('Purchase_Date')
            model.Price = request.POST.get('Price')
            model.save()
            message = "Seedlings or crops recorded"
            return render(request, 'seedcrop.html', {'form': form, 'message': message, 'seedlings': seedlings})
    except:
        message = "Is date or format correct?"
        return render(request, 'seedcrop.html', {'form': form, 'message': message, 'seedlings': seedlings})
    return render(request, 'seedcrop.html', {'form': form, 'seedlings': seedlings})


def sales(request):
    form = SalesForm()
    sales_made = Sales.objects.all()

    try:
        if request.method == 'POST':
            model = Sales()
            model.Sales_ID = request.POST.get('Sales_ID')
            model.Product_Sold = request.POST.get('Product_Sold')
            model.Quantity_Sold = request.POST.get('Quantity_Sold')
            model.Sales_Made = float(request.POST.get('Price')) * float(request.POST.get('Quantity_Sold'))
            model.Date = request.POST.get('Date')
            model.Price = request.POST.get('Price')
            model.save()
            message = "Sales Recorded"
            return render(request, 'sales.html', {'form': form, 'message': message, 'sales': sales_made})
    except:
        message = "Enter correct date or date format YYYY-MM-DD"
        return render(request, 'sales.html', {'form': form, 'message': message, 'sales': sales_made})
    return render(request, 'sales.html', {'form': form, 'sales': sales_made})


def update_mobile(request):
    if Employee.objects.filter(Employee_ID=request.POST.get('Employee_ID')).exists():
        mobile = Employee.objects.get(Employee_ID=request.POST.get('Employee_ID'))
        mobile.Mobile_Number = request.POST.get('Mobile_Number')
        mobile.save()
        message = "Mobile Number Changed!"
        return redirect('/')
    else:
        return redirect('/employe')


def update_salary(request):
    if Employee.objects.filter(Employee_ID=request.POST.get('Employee_ID')).exists():
        salary = Employee.objects.get(Employee_ID=request.POST.get('Employee_ID'))
        salary.Salary = request.POST.get('Salary')
        salary.save()
        message = "Salary Changed!"
        return redirect('/')
    else:
        return redirect('/employe')



def update_terminationdate(request):
    if Employee.objects.filter(Employee_ID=request.POST.get('Employee_ID')).exists():
        termdate = Employee.objects.get(Employee_ID=request.POST.get('Employee_ID'))
        termdate.Mobile_Number = request.POST.get('Termination_Date')
        termdate.save()
        message = "Employee contract termination has been updated."
        return redirect('/')
    else:
        return redirect('/employe')


def update_email(request):
    if Employee.objects.filter(Employee_ID=request.POST.get('Employee_ID')).exists():
        mail = Employee.objects.get(Employee_ID=request.POST.get('Employee_ID'))
        mail.Mobile_Number = request.POST.get('E_mail')
        mail.save()
        return redirect('/')
    else:
        return redirect('/employe')