from django.shortcuts import render , redirect
from . import models
from . import forms

from django.http import HttpResponse
# Create your views here.

# start department

def returnDepartment(request):
    x = models.Department.objects.all()
    context={
        'Departments' : x,
    }
    return render(request, 'Bookapp/listalldepartment.html',context)

 
def DapartmentDesplay(request,id):
    dept = models.Department.objects.get(id=id)
    context={
        'Department' : dept,
    }
    return render(request, 'Bookapp/department.html',context)

# end department

#start Book
def Add_New_Department(request):
    form = forms.DepartmentForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return redirect('list_all_department')
    
    context = {
        'form' : form,
    }
    
    return render(request, 'Bookapp/NewDepartment.html' , context)
#end Book


def Add_newBook(request,id):
    dept = models.Department.objects.get(id=id)
    
    form = forms.BookForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form = form.save(commit=False)
        form.dept = dept
        form.save()
        return redirect('Department',id=id) 
    context={
        'Department' : dept,
        'form':form,
    }
    return render(request, 'Bookapp/NewBook.html',context)
