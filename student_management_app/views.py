from django.shortcuts import render, redirect
from . models import Student, Hobby
from django.db.models import Q
import os

# Create your views here.

def home(request):
    all_student = Student.objects.all()

    if request.method == 'GET':
        data = request.GET.get('src')
        if data:
            all_student = Student.objects.filter(Q(name__icontains = data) | Q(email__icontains = data))
            # print(all_stdudent))
    return render(request, 'index.html',{'stu': all_student})


def delete_prof(request, id):
    all_student = Student.objects.get(id=id)

    if all_student.image != 'def.png':
        os.remove(all_student.image.path)
    all_student.delete()
    return redirect('home')

def create_profile(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        image = request.FILES['image']
        mother_name = request.POST['mother_name']
        father_name = request.POST['father_name']
        religion = request.POST['religion']
        date_of_birth = request.POST['date_of_birth']
        roll = request.POST['roll']
        city = request.POST['city']
        is_Bangladeshi = request.POST.get('is_Bangladeshi') == 'on'
        age = request.POST['age']
        hobby = request.POST['hobby']

        stu_hobby = Hobby.objects.create(name=hobby)
        stu_hobby.save()
        
        student = Student(name=name, email=email, image=image, mother_name=mother_name, father_name=father_name, religion=religion, date_of_birth=date_of_birth, roll=roll, city=city, is_Bangladeshi=is_Bangladeshi, age=age, hobby=stu_hobby)
        student.save()
        return redirect('home') 


    return render(request, 'create.html')