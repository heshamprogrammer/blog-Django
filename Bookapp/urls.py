from . import views
from django.urls import path,include

urlpatterns = [
    path('Dept_All',views.returnDepartment , name='list_all_department'),
    path('Department/<int:id>',views.DapartmentDesplay , name='Department'),
    path('Add_Department',views.Add_New_Department , name='add_new_department'),
    path('Department/<int:id>/NewBook',views.Add_newBook , name='NewBook'),

]
