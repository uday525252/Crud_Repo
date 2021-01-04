from django.shortcuts import render,redirect

from testapp.models import Employee

from testapp.forms import EmployeeForm

# Create your views here.

def read_data_view(request):
    employee_list=Employee.objects.all()
    my_dict={'employee_list':employee_list}
    return render(request,"read.html",my_dict)

def insert_data_view(request):
    form=EmployeeForm()
    my_dict={'form':form}
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/home')

    return render(request,"insert.html",my_dict)

def delete_data_view(request,id):
    employee_list=Employee.objects.get(id=id)
    employee_list.delete()
    return redirect('/home')


def update_data_view(request,id):
    employee_data=Employee.objects.get(id=id)
    my_dict={'employee_data':employee_data}
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee_data)
        if form.is_valid():
            form.save()
        return redirect("/home")





    return render(request,"update.html",my_dict)
