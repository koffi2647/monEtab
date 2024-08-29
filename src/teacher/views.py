from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import TeacherForm
from .models import Teacher
# Create your views here.
def index(request):
    teachers = Teacher.objects.all()
    context = { 'teachers': teachers }
    
    return render(request,'teacher/indexTeacher.html',context)

def ajouterTeacher(request):
    
    if request.method == "POST":
        print(request.POST)
        form = TeacherForm(request.POST)
        
        if form.is_valid():
           print(form.cleaned_data)
           form.save()
           return redirect('teacher:index')
        else:
            return render(request, 'teacher:modifierTeacher', context)  
    form = TeacherForm()
    context = {'form': form}
    return render(request, 'teacher/ajouterTeacher.html', context)

def modifierTeacher(request,id):
    teacher = Teacher.objects.get(id=id)
    context = {'title':'modification teacher'}
    
    if request.method == 'POST':
        form = TeacherForm(request.POST , instance = teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher:index')
    
    form = TeacherForm(instance = teacher)
    context = {'form': form}
    return render(request, 'teacher/modifierTeacher.html', context)   

def suprimer (request, id):
    teacher = Teacher.objects.get(id = id)
    teacher.delete()
    return redirect('teacher:index')