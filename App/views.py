from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from App.forms import NewStudentForm, StudentUpdateForm
from App.models import Student
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# our homepage.
def index(request):
    context = {"user": request.user, "state": True}
    return render(request, "App/index.html", context)


# get all student records.
@login_required
def all_students(request):
    if request.method == "GET":
        students = Student.objects.all()
        if students:
            context = {"data": students, "state": False}
            return render(request, "App/allStudents.html", context)
        else:
            context = {"message": "No student records found", "option": "add"}
            return render(request, "App/404.html", context)
    else:
        context = {"message": "POST is not allowed!"}
        return render(request, "App/404.html", context)


# adds a new student record to the database.
@login_required
def add_student(request):
    if request.method == "POST":
        student_form = NewStudentForm(request.POST)
        if student_form.is_valid():
            cd = student_form.cleaned_data
            # std = get_object_or_404(Student,Registration=cd['Registration'])
            if Student.objects.filter(Registration=cd["Registration"]).exists():

                # get the instance to send to error page
                student = Student.objects.get(Registration=cd["Registration"])

                context = {"message": "Student already exists!", "data": student}
                return render(request, "App/404.html", context)
            else:
                student_form.save()
                student_data = Student.objects.get(Registration=cd["Registration"])
                # print(
                #     "{} : {}".format(student_data.FirstName, student_data.Registration)
                # )
                context = {"data": student_data}
                return render(request, "App/studentDetails.html", context)
        else:
            context = {"message": "Invalid form! Try to add again."}
            return render(request, "App/404.html", context)
    else:
        return HttpResponse("GET is not allowed!")


# updates our student records.
@login_required
def update_student(request, slug):
    if request.method == "POST":
        student_update_form = StudentUpdateForm(request.POST)
        if student_update_form.is_valid():
            cd = student_update_form.cleaned_data
            Student.objects.filter(slug=slug).update(
                FirstName=cd["FirstName"],
                SecondName=cd["SecondName"],
                Registration=cd["Registration"],
                Hostel=cd["Hostel"],
                LaptopSerialNumber=cd["LaptopSerialNumber"],
            )      
            # send message to front-end using dajngo messages frmaework.
            messages.info(request, "{} {} updated successfully!".format(cd["FirstName"],cd["SecondName"]))
            return redirect("index")

        else:
            context = {"message": "Form submitted is invalid"}
            return render(request, "App/404.html", context)
    else:
        context = {"message": "GET is not allowed!"}
        return render(request, "App/404.html", context)


# deletes student instance.
@login_required
def delete_student(request, reg):
    student = Student.objects.get(slug=reg)
    student.delete()
    messages.info(request, "{} deleted successfully!".format(student.FirstName))
    return redirect("index")


# searches databases for student with unipue slug.
@login_required
def search_student(request, reg):
    if request.method == "GET":
        try:
            student = Student.objects.get(slug__exact=reg)
            if student:
                context = {"data": student, "state": False}
                return render(request, "App/studentDetails.html", context)
        except:
            context = {"message": "Student not found"}
            return render(request, "App/404.html", context)
    else:
        context = {"message": "POST is not allowed!"}
        return render(request, "App/404.html", context)

