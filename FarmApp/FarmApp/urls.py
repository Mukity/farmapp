from django.urls import path
from farmapp import views

urlpatterns = [
    path('login', views.login),
    path('logout', views.log_out),
    path('', views.home),
    path('employees', views.employees),
    path('chemicals_fertilizers', views.chemicals_fertilizers),
    path('seedling_crop', views.seedling_crop),
    path('sales', views.sales),
    path('update_mobile', views.update_mobile),
    path('update_salary', views.update_salary),
    path('update_terminationdate', views.update_terminationdate),
    path('update_email', views.update_email)
]
