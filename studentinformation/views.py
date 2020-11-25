from django.shortcuts import render
from django.http import HttpResponse
from studentinformation.models import Students, Courses, Enrollment
from django.core.paginator import Paginator
from django.contrib.auth.decorators  import login_required

# Create your views here.

@login_required
def home(request):
    studentinformation=Students.objects.all()
    coursedata=Courses.objects.all()
    return render(request, "studentinformation/home.html",{'studentinformation':studentinformation,'courses':coursedata})

@login_required
def students(request):
    studentinformation=Students.objects.all()
    paginator = Paginator(studentinformation, 10)
    page = request.GET.get('page')
    studentdata = paginator.get_page(page)
    print (studentinformation)
    return render (request, "studentinformation/students.html",{"data":studentdata})

@login_required
def courses(request):
    studentinformation=Courses.objects.all()
    paginator = Paginator(studentinformation, 10)
    page = request.GET.get('page')
    coursedata = paginator.get_page(page)
    print (studentinformation)
    return render (request, "studentinformation/courses.html",{"data":coursedata})

@login_required
def enrollment(request):
    studentinformation = Students.objects.all()
    coursedata = Courses.objects.all()
    enrollmentdata= ''
    if('studentid' in request.session):
        enrollmentdata= Enrollment.objects.filter(studentid = request.session['studentid'])
    if('sname' in request.GET and 'cotitle' not in request.GET):
        sname = request.GET.get('sname')
        request.session['studentid'] = sname
        return HttpResponse('Success')
    if('sname' in request.GET and 'cotitle' in request.GET):
        sname = request.GET.get('sname')
        cotitle = request.GET.get('cotitle')
        enrollmentdata = Enrollment.objects.filter(studentid = sname)
        for row in enrollmentdata:
            if row.coursetitle == cotitle:
                return HttpResponse('Error')
        newdata = Enrollment(studentid = sname, coursetitle = cotitle)
        newdata.save()
        return HttpResponse("Success")
    return render(request, 'studentinformation/enrollment.html',{'studentinformation':studentinformation, 'courses':coursedata,'enrollment':enrollmentdata})
