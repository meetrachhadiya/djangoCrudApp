from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import *
from .forms import *
from django.db.models import Q
# Create your views here.

def homepage1(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if "add" in request.POST:
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                standard = form.cleaned_data['standard']
                Student.objects.create(name = name , email = email, standard = standard)
                # form.save()
                messages.success(request, "Student Added Successfully!!")
                form = StudentForm()
        elif "delete" in request.POST:
            id = request.POST.get("id")
            Student.objects.get(id = id).delete()
            messages.warning(request, "Student Deleted Succesfully!!")    
            form = StudentForm()
    else:
        form = StudentForm()

    students = Student.objects.order_by("id")
    p = Paginator(students, 6)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {"page_obj": page_obj, "form" : form, "students" : students}
    # sending the page object to index.html
    return render(request, 'index2.html', context)

def update_student(request, id):
    if request.method == "POST":
        student = Student.objects.get(id=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Update Student successfully!")
            return HttpResponseRedirect("/")
    else:
        student = Student.objects.get(id=id)
        form = StudentForm(instance=student)
    return render(request, "edit_student.html", {"form" : form})


def homepage(request):
    students = Student.objects.all()

    if request.method=="POST":
        if "add" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            standard = request.POST.get("standard")
            # grade_id = request.POST.get("grade")  # Get the grade id from the form
            # grade = get_object_or_404(Grade, id=grade_id) 
            Student.objects.create(name = name , email = email, standard = standard) 
            messages.success(request, "Student Added Successfully!!")

        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            email = request.POST.get("email")
            
            student = Student.objects.get(id = id)
            student.name = name
            student.email = email
            student.save()
            messages.success(request, "Student Updated Successfully!!")

        elif "delete" in request.POST:
            id = request.POST.get("id")
            Student.objects.get(id = id).delete()
            messages.warning(request, "Student Deleted Succesfully!!")

        elif "search" in request.POST:
            data = request.POST.get("search")
            print(data)
            students = students.filter(
                Q(name__icontains = data) |
                Q(standard__icontains = data) |
                Q(email__icontains = data) 
            )

    context = {"students" : students}
    return render(request, "index.html", context)