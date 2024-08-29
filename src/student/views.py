from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Student
from .forms import StudentForm

# Create your views here.
def index(request):
    
    students = Student.objects.all()
    context = { 'students': students }
    
    return render(request, 'student/indexStudent.html',context)

def ajoutStudent(request):
    
    if request.method == "POST":
        print(request.POST)
        form = StudentForm(request.POST)
        
        if form.is_valid():
            
            print(form.cleaned_data)
            form.save()
            return redirect('student:index')
        else:
            return render(request, 'student:modifierStudent', context)        
    form = StudentForm()
    context = {'form': form}
    return render(request, 'student/ajouterstudent.html', context) 

def modifierStudent(request,id):
    student = Student.objects.get(id=id)
    context = {'title':'modification eleve'}
    
    if request.method == 'POST':
        form = StudentForm(request.POST , instance = student)
        if form.is_valid():
            form.save()
            return redirect('student:index')
        
    
    form = StudentForm(instance = student)
    context = {'form': form}
    return render(request, 'student/modifierStudent.html', context)   

def suprimer (request, id):
    student = Student.objects.get(id = id)
    student.delete()
    return redirect('student:index')