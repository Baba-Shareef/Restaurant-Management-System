from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from administrator.models import Subjects,Enroll_subjects
# Create your views here.
def home(request):
     return render(request,"home.html")


def course(request):
     sub = Subjects.objects.all()
     return render(request,'course.html',{'courses':sub})


def profile(request):
     return render(request,'profile.html')
def enroll(request, id):
    # Fetch the subject using the id
    subject = get_object_or_404(Subjects, id=id)

    # Create a new enrollment
    new_enroll = Enroll_subjects(
        Subject=subject.Subject,  # Use the subject instance for course
        Professor=subject.Professor,  # Access the professor field from the subject instance
        Credits=subject.Credits  # Access the credits field from the subject instance
    )
    new_enroll.save()  # Save the new enrollment to the database
#    obj = Enroll_subjects.objects.all()
    # Render the RegisteredCourse template, passing the new_enroll object
    return redirect('Course')


def unenroll(request,id):
    subject = get_object_or_404(Enroll_subjects, id=id)
    subject.delete()
    return redirect('RegisteredCourse')
def RegisteredCourse(request):
    sub = Enroll_subjects.objects.all()
    return render(request,'RegisteredCourse.html',{'subjects':sub})


def noti(request):
    return HttpResponse("hello")