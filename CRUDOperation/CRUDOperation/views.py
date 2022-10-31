from django.shortcuts import render
from CRUDOperation.models import EmpModel
from django.contrib import messages
from CRUDOperation.forms import EmployeeForm
def showemp(request):
    showall=EmpModel.objects.all()
    return render(request,"index.html",{"data":showall})

def insert(request):
    if request.method=="POST":
        if request.POST.get('id') and request.POST.get('ename') and request.POST.get('contact') and request.POST.get('salary') and request.POST.get('gender'):
            saverecord=EmpModel()
            saverecord.id=request.POST.get('id')
            saverecord.ename=request.POST.get('ename')
            saverecord.contact=request.POST.get('contact')
            saverecord.salary=request.POST.get('salary')
            saverecord.gender=request.POST.get('gender')
            saverecord.save()
            messages.success(request, 'Employee' + saverecord.ename + 'Is Saved Successfully..!')
            return render(request,"insert.html")
        else:
            return render(request,"insert.html")
    return render(request,"insert.html")

def updateemp(request, id):
    editempobj=EmpModel.objects.get(id=id)
    return render(request,"update.html",{"EmpModel":editempobj})

def editemp(request, id):
    updateempobj=EmpModel.objects.get(id=id)
    forms=EmployeeForm(request.POST, instance=updateempobj)
    if forms.is_valid():
        forms.save()
        messages.success(request, 'Record Updated Successfully..!')

        return render(request,"update.html",{"EmpModel":updateempobj})

def delete(request, id):
    deleteempobj=EmpModel.objects.get(id=id)
    deleteempobj.delete()
    showdata=EmpModel.objects.all()
    return render(request,"index.html",{"data":showdata})